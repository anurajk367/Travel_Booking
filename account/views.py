from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,FormView,CreateView,ListView,TemplateView,DetailView
from .forms import*
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import  never_cache
from django.utils.decorators import method_decorator
from account.models import Packages,Event,Intrested,Booked
from django.utils import timezone
from datetime import timedelta


# Create your views here.


def signin_requierd(fn):
    def inner(requiest,*args,**kwargs):
        if requiest.user.is_authenticated:
            return fn(requiest,*args,**kwargs)
        else :
            messages.error(requiest,"Login first")
            return redirect("log")
    return inner
decs=[never_cache,signin_requierd]

    
class Logview(FormView):
    template_name="login.html"
    form_class=Loginform
    def post(self,request,*args,**kwrgs):
        form_data=Loginform(data=request.POST)
        if form_data.is_valid():
            us = form_data.cleaned_data.get("username")
            pswd = form_data.cleaned_data.get("password")
            user=authenticate(request,username=us,password=pswd)
            if user:
                login(request,user)
                messages.error(request,"sign in Successfull..!")
                return redirect('h')
            
            else:
                messages.error(request,"sign in faild")
                return redirect("log")
        return render (request,"log.html",{"form":form_data})
        

class Regview(CreateView):
    template_name="reg.html"
    form_class=Regform
    model=User
    success_url=reverse_lazy("h")



class Logoutview(View):
    def get (self,request):
        logout(request)
        return  redirect("log")
    


class Homeview(ListView):
    template_name="home.html"
    queryset=Packages.objects.all()
    context_object_name="packages"




class Abotview(TemplateView):
    template_name="about.html"
   
    


class Contactview(View):
    def get (self,request):
        return render(request,'contact.html')
    


@method_decorator(decs,name='dispatch')
class Bookinview(View):
    def get (self,request):
        return render(request,'booking.html')
    

    
@method_decorator(decs,name='dispatch')
class Cretaepackageview(View):
    def get (self,request):
        return render(request,'createpackage.html')
    

    
class Toursview(ListView):
    template_name="tours.html"
    queryset=Packages.objects.all()
    context_object_name="packages"




@method_decorator(decs,name='dispatch')
class Tourdetailview(DetailView):
    template_name="tour-details.html"
    pk_url_kwarg='id'
    queryset=Packages.objects.all()
    context_object_name="packages"



@signin_requierd
def intested_pack(request,*args,**kwargs):
    id=kwargs.get("id")
    pack=Packages.objects.get(id=id)
    user=request.user
    members=request.POST.get("mbrs")
    name=request.POST.get("name")
    email=request.POST.get("email")
    message=request.POST.get("message")
    phone=request.POST.get("phn")
    date=request.POST.get("dte")
    Intrested.objects.create(package=pack,user=user,memberes=members,date=date,name=name,message=message,email=email)
    messages.success(request,"Added to intrest")
    return redirect("h")


def Removeintrest(request,**kwargs):
    pid=kwargs.get("id")
    int=Intrested.objects.get(id=pid)
    int.delete()
    messages.success(request," Remove Package From Intrested List")
    return redirect('inpackage')


class Upcomingeventview(ListView):
    template_name="upcomingevents.html"
    def get_queryset(self) -> QuerySet[Any]:   
        current_date = timezone.now()
        dt = current_date + timedelta(days=10)
        queryset=Event.objects.filter(date__lt=dt,date__gt=current_date)
        return queryset
    context_object_name="events"
  
    




    
@method_decorator(decs,name='dispatch')    
class Mytripview(ListView):
    template_name="mytrip.html"
    queryset=Intrested.objects.all()
    context_object_name="mytrip"

    def get_queryset(self):
        return Booked.objects.filter(user=self.request.user)
    



@method_decorator(decs,name='dispatch')    
class Mytripdetail(DetailView):
    template_name="mytripdetail.html"
    pk_url_kwarg='id'
    queryset=Booked.objects.all()
    context_object_name="book"

    def get_queryset(self):
        return Booked.objects.filter(user=self.request.user)
    


@method_decorator(decs,name='dispatch')    
class Intrestedpackagview(ListView):
    template_name="intrestedpackages.html"
    queryset=Intrested.objects.all()
    context_object_name="intrested"

    def get_queryset(self):
        return Intrested.objects.filter(user=self.request.user)




@method_decorator(decs,name='dispatch')    
class Intrestedpackagedetailview(DetailView):
    template_name="inpackagedetail.html"
    pk_url_kwarg='id'
    queryset=Intrested.objects.all()
    context_object_name="int"

    def get_queryset(self):
        return Intrested.objects.filter(user=self.request.user)

 



@method_decorator(decs,name='dispatch')
class Paymentview(TemplateView):
    template_name="payment.html"


    def post(self,request,*args,**kwargs):
        Pid=kwargs.get("id")
        int=Intrested.objects.get(id=Pid)
        user=request.user
        ad=request.POST.get("adrs")
        phn=request.POST.get("phn")
        Booked.objects.create(package=int.package,address=ad,user=user,phone=phn)
        print('success')
        # pack.objects.delete()
        messages.success(request,"order placed..!")
        return redirect("inpackage")
    
    

