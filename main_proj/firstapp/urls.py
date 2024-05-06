from django.urls import path
from django.urls.resolvers import URLPattern
from .views import UserProfileView
from . import views

urlpatterns=[
    path('',views.product_list,name='Index'),
    path('',views.images_list,name='Index'),
    path('categories/',views.category_list_view,name='categories'),
    path('categories/rent_product/',views.rent_product,name='rent_product'),
    path('Profile/<int:id>',UserProfileView.as_view(),name='Profile'),
    path('Profile/update_profile/',views.update_profile,name='update_profile')
]