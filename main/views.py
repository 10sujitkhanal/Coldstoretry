from django.shortcuts import render
from accounts.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login')
def index(request):
    farmer = Farmer.objects.all()
    context = {
        'farmers': farmer
    }
    return render(request,"index.html", context)

@login_required(login_url='/accounts/login')
def farmers(request, id):
    farmers = Farmer.objects.get(farmer=id)
    context = {
        'farmers':farmers,
    }
    return render(request, "farmers.html", context )

@login_required(login_url='/accounts/login')
def seat(request, id):
    farmer = Farmer.objects.get(farmer=id)
    seat = Bookings.objects.filter(farmer=id)
    return render(request,"seat.html", {'farmer':farmer, 'seat':seat})    

@login_required(login_url='/accounts/login')
def booked(request):
    if request.method == 'POST':
        user = request.user
        seat = ','.join(request.POST.getlist('check'))
        farmer_id = request.POST['farmer_id']
        book = Bookings(useat=seat, farmer_id=farmer_id, user=user)
        book.save()
        return HttpResponseRedirect('/')    
        

