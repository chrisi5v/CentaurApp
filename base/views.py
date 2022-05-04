from django.shortcuts import render, redirect
from django.contrib  import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import ChecklistForm
from .models import VehicleChecklist, Vehicle, User
from django.http import HttpResponse



def loginPage(request):
    status = 'loggedout'
    if request.user.is_authenticated:
        status = 'loggedin'
        return redirect('home')

    if  request.method == 'POST':
        username =  request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user =  authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid User')
    context = {'status':status}
    return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def createChecklist(request):
    form = ChecklistForm()
    if request.method == 'POST':
        VehicleChecklist.objects.create(
            driver = User.objects.get(id=request.user.id),
            vehicle  =  Vehicle.objects.get(id=request.user.vehicle.id),
            brakes = True  if  request.POST.get('brakes')  ==  'on' else  False,
            wipers = True if request.POST.get('wipers')   ==  'on' else  False,
            tires = True if request.POST.get('tires')  ==  'on' else  False,
            oil =  True if request.POST.get('oil')  ==  'on' else  False,
            gas =  True if request.POST.get('gas')  ==  'on' else  False,
            seatbelt = True if request.POST.get('seatbelt')  ==  'on' else  False,
            comment = request.POST.get('comment')
        )
        return redirect('home')
    context = {'form':form}
    return render(request, 'base/checklist_form.html', context)

def  updateChecklist(request,pk):
    checklist  = VehicleChecklist.objects.get(id=pk)
    form = ChecklistForm(instance = checklist)

    if request.user != checklist.driver:
        return HttpResponse('You dont have permission to perform this action')

    if request.method ==  'POST':
        checklist.driver = User.objects.get(id=request.user.id)
        checklist.vehicle  =  Vehicle.objects.get(id=request.user.vehicle.id)
        checklist.brakes = True  if  request.POST.get('brakes')  ==  'on' else  False
        checklist.wipers = True if request.POST.get('wipers')   ==  'on' else  False
        checklist.tires = True if request.POST.get('tires')  ==  'on' else  False
        checklist.oil =  True if request.POST.get('oil')  ==  'on' else  False
        checklist.gas =  True if request.POST.get('gas')  ==  'on' else  False
        checklist.seatbelt = True if request.POST.get('seatbelt')  ==  'on' else  False
        checklist.comment = request.POST.get('comment')
        checklist.save()
        return redirect('home')
    context = {'form':form}
    return render(request, 'base/checklist_form.html', context)

def  viewChecklist(request,pk):
    checklist  = VehicleChecklist.objects.get(id=pk)
    form = ChecklistForm(instance = checklist)
    context = {'form':form, 'checklist':checklist}
    return render(request, 'base/checklist_view.html', context)

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    checkLists = VehicleChecklist.objects.all()
    alerts = VehicleChecklist.objects.filter(Q(brakes__icontains=0)|
                                             Q(wipers__icontains=0)|
                                             Q(tires__icontains=0)|
                                             Q(oil__icontains=0)|
                                             Q(gas__icontains=0)|
                                             Q(seatbelt__icontains=0))
    alert_count = alerts.count
    context = {'checkLists':checkLists, 'alerts':alerts,'alert_count':alert_count}
    return render(request, 'base/home.html', context)