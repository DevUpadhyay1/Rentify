from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns=[
    path('',views.Index,name='Index'),
    path('categories/',views.category_list_view,name='categories'),
    path('rent/',views.rent,name='rent'),
    
]