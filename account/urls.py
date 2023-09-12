from django.urls import path
from .views import*


urlpatterns=[
    
    path('reg',Regview.as_view(),name='reg'),
    path('home',Homeview.as_view(),name='h'),
    path('logout',Logoutview.as_view(),name='logout'),
    path('about',Abotview.as_view(),name='about'),
    path('tours',Toursview.as_view(),name='tours'),
    path('contact',Contactview.as_view(),name='contact'),
    path('tourdetail/<int:id>',Tourdetailview.as_view(),name='tourdetail'),
    path("intrest/<int:id>",intested_pack,name="intrest"),
    path('booking',Bookinview.as_view(),name='booking'),
    path('cpackage',Cretaepackageview.as_view(),name='cpackage'),
    path('upevent',Upcomingeventview.as_view(),name='upevent'),
    path('mytrip',Mytripview.as_view(),name='mytrip'),
    path('inpackage',Intrestedpackagview.as_view(),name='inpackage'),
    path('inpackagedetail/<int:id>',Intrestedpackagedetailview.as_view(),name='inpackagedetail'),
    path('payment/<int:id>',Paymentview.as_view(),name='payment'),
    path('removeint/<int:id>',Removeintrest,name='removeint'),
    path('mytripdetail/<int:id>',Mytripdetail.as_view(),name='mytripdetail'),


    

]