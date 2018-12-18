from.views import Index,addtodo,completetodo,deletecomplete,deleteall
from django.urls import path

urlpatterns = [
    path('',Index,name='index'),
    path('add/',addtodo,name='add'),
    path('complate/<todo_id>',completetodo,name='complete'),
    path('deletecomplete',deletecomplete,name='deletecomplete'),
    path('deleteall',deleteall,name='deleteall'),


]
