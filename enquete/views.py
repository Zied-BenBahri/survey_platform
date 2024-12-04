from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from django.core.paginator import Paginator


def enquete_map(request):
    if not(request.user.is_authenticated):
        return redirect('/error_page')
    #enquetes = list(Enquete.objects.exclude(latitude__isnull=True).exclude(longitude__isnull=True).values('latitude', 'longitude'))
    #
    """
    if not(request.user.is_staff):
        enquetes = list(Enquete.objects.filter(agent__user=request.user).exclude(latitude__isnull=True).exclude(longitude__isnull=True).values('created_at','pk','latitude', 'longitude'))
    else:
        enquetes = list(Enquete.objects.exclude(latitude__isnull=True).exclude(longitude__isnull=True).values('created_at','pk','latitude', 'longitude'))
    #print(enquetes)"""
    
    enquetes = list(Enquete.objects.exclude(latitude__isnull=True).exclude(longitude__isnull=True).values('created_at','pk','latitude', 'longitude'))

    context = {
        "enquetes" : enquetes
    }
    return render(request,"enquete/map.html",context) 


def load_localites(request):
    delegation_id = request.GET.get('delegation_id')
    localites = Localite.objects.filter(delegation_id=delegation_id).order_by('libelle')
    return render(request, 'enquete/localite_dropdown_list_options.html', {'localites': localites})



def enquete_detail(request,pk):
    if not(request.user.is_authenticated):
        return redirect('/error_page')
    enquete = Enquete.objects.get(id=pk)
    context = {
        "enquete": enquete
    }
    return render(request,"enquete/enquete_detail.html",context) 


def enquete_list(request):
    if not(request.user.is_authenticated):
        return redirect('/error_page')
    if not(request.user.is_staff):
        enquetes = Enquete.objects.filter(agent__user=request.user).order_by('-created_at') #####################################
    else :
        enquetes = Enquete.objects.all().order_by('-created_at')
    p = Paginator(enquetes,7)
    page = request.GET.get('page')
    enquetes_list = p.get_page(page)
    context = {
        
        "enquetes_list":enquetes_list,
    }
    return render(request,"enquete/enquete_list.html",context)
 
def enquete_create(request):
    if not(request.user.is_authenticated):
        return redirect('/error_page')
    # ------ 
    """
    try:
        agent = Agent.objects.get(user=request.user)
    except Agent.DoesNotExist:
        return redirect('/error_page') """ # ------
    if request.method == "POST" :
        form = EnqueteForm(request.POST,user=request.user) 
        if form.is_valid():
            #messages.success(request, 'Enquête créée avec succès!')
            form.save()
            return redirect("/enquete/list")
        else: 
            for error in form.errors.values():
                messages.error(request,error)
    else:
        form = EnqueteForm(user=request.user)
    return render(request,"enquete/enquete_create.html",{'form': form})
