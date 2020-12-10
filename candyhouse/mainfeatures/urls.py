from django.urls import path
from mainfeatures import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info/<int:member_id>', views.info, name='info'),
    path('detail_info', views.detail_info, name='detail_info'),
]