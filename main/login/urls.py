from . import views
from django.urls import path

urlpatterns=[
    path("",views.login,name='login'),
    path('home',views.home,name='home'),
    path('admine',views.admine,name='admine'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path("delete/<int:id>/",views.delete,name="delete" ),
    path("update/<int:id>/",views.update,name='update'),
    path('search',views.search,name='search'),
    path('addusr',views.addusr,name='addusr')

    
]