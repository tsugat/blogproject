#from django.contrib import admin
from django.urls import path
#from .views import BlogList, BlogDetail ,BlogCreate,BlogDelete,BlogUpdate
from .views import BlogList, BlogDetail ,BlogCreate,BlogDelete,BlogUpdate,BlogStudy

urlpatterns = [
    path('list/', BlogList.as_view(), name='list'),
    path('detail/<int:pk>/', BlogDetail.as_view(), name='detail'),
    #↑<int:pk>がテーブルのどの行をもってくるのかの指定になっている。とのこと。pkはprimary keyのこと。
    path('create/', BlogCreate.as_view(), name='create'),
    path('delete/<int:pk>', BlogDelete.as_view(), name='delete'),
    path('update/<int:pk>', BlogUpdate.as_view(), name='update'),

    #tsugat start
    path('study/', BlogStudy.as_view(), name='study'),
    #tsugat end
]

