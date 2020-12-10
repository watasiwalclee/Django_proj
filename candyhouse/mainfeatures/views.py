from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from mainfeatures import models

# Create your views here.
def index(request):
    members = models.Member.objects.all()
    
    output = []
    for member in members:
        mb = {}
        mb['id'] = member.id
        mb['name'] = member.name
        mb['in_battle'] = member.in_battle
        mb['compensate'] = member.compensate
        mb['rec'] = ['還沒出','還沒出','還沒出']
        for i,rec in enumerate(member.record_set.filter(compensate=0).order_by('turn')):
            if rec.week != 0 and rec.num != 0:
                mb['rec'][i] = str(rec.week)+'-'+str(rec.num)
        output.append(mb)
    
    context = {
        'members':output
    }

    return render(request, 'index.html',context=context)

def info(request, member_id):

    def stringToint(s):
        if type(s) == str:
            s = s.strip()
            return int(s) if s else 0
        elif type(s) == int:
            return s

    if request.method == 'GET':
        request.session['member_id'] = member_id
        member = models.Member.objects.get(id=member_id)

        com_dict = {False:0, True:1}
        
        records = [[],[],[]]
        for i in range(3):
            for j in range(2):
                records[i].append({'week':'','num':'','dmg':'','ending':''})

        for r in member.record_set.all().order_by('turn'):
            records[stringToint(int(r.turn))-1][r.compensate]['week'] = r.week 
            records[stringToint(int(r.turn))-1][r.compensate]['num'] = r.num 
            records[stringToint(int(r.turn))-1][r.compensate]['dmg'] = r.damage
            records[stringToint(int(r.turn))-1][r.compensate]['ending'] = r.ending

        context = {
            'member':member,
            'records': records
        }

        return render(request, 'information.html',context=context)

    elif request.method == 'POST':
        print(request.POST)
        ud_member_id = request.session['member_id']
        member = models.Member.objects.get(id=ud_member_id)
        
        # 更新成員狀態
        member.in_battle = 'in_battle' in request.POST
        member.compensate = 'compensate' in request.POST
        member.save()

        # 更新紀錄
        for i in range(1,4):
            for c in [True,False]:
                queryrecs = models.Record.objects.filter(uid=ud_member_id).filter(turn=i).filter(compensate=c)
                if len(queryrecs) != 0:
                    if c == False:
                        rec = queryrecs[0]
                        rec.week = request.POST['week{}'.format(i)]
                        rec.num = request.POST['num{}'.format(i)]
                        rec.damage = request.POST['dmg{}'.format(i)]
                        rec.ending = 'check_end{}'.format(i) in request.POST
                        rec.save()
                    else:
                        rec = queryrecs[0]
                        rec.week = request.POST['week{}compensate'.format(i)]
                        rec.num = request.POST['num{}compensate'.format(i)]
                        rec.damage = request.POST['dmg{}compensate'.format(i)]
                        rec.save()
                else:
                    if c == False:
                        models.Record.objects.create(
                            uid=models.Member.objects.get(uid=ud_member_id),
                            turn=i,
                            week=stringToint(request.POST['week{}'.format(i)]),
                            num=stringToint(request.POST['num{}'.format(i)]),
                            damage=stringToint(request.POST['dmg{}'.format(i)]),
                            ending='check_end{}'.format(i) in request.POST,
                            compensate=0
                        )
                    else:
                        models.Record.objects.create(
                            uid=models.Member.objects.get(uid=ud_member_id),
                            turn=i,
                            week=stringToint(request.POST['week{}compensate'.format(i)]),
                            num=stringToint(request.POST['num{}compensate'.format(i)]),
                            damage=stringToint(request.POST['dmg{}compensate'.format(i)]),
                            compensate=1
                        )

        return HttpResponseRedirect(reverse('mainfeatures:index'))
        

def detail_info(request):
    output_list = []
    members = models.Member.objects.all()
    for member in members:
        member_dict = {}
        member_dict['name'] = member.name
        member_dict['rec'] = []
        
        for i in range(1,4):
            rec = member.record_set.filter(turn=i).order_by('compensate')
            rec_dict = {}
            for ri,r in enumerate(rec):
                #print(member.name,ri,str(r.week)+'-'+str(r.num),r.damage)
                if ri == 0:
                    rec_dict['damage']=r.damage
                    rec_dict['week']=str(r.week)+'-'+str(r.num)
                elif ri == 1:
                    rec_dict['com_damage']=r.damage
                    rec_dict['com_week']=str(r.week)+'-'+str(r.num)

            member_dict['rec'].append(rec_dict)
        output_list.append(member_dict)
    context = {
        'output_list':output_list
    }

    return render(request, 'detail_info.html', context=context)