from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Horse, Race, Expense
from .filters import RaceFilter, ExpenseFilter
from .forms import CreateHorseForm, CreateRaceForm, CreateExpenseForm, SellHorseForm
from django.contrib.auth.models import User
from django.contrib import messages


def add_horse(request):
    submitted = False
    if request.method =="POST":
        form = CreateHorseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_horse?submitted=True')
    else:
        form = CreateHorseForm
        if 'submitted' in request.GET:
            submitted = True

    #list = horseData.objects.all()

    return render(request, 'Horse/add_horse.html',{'form':form, 'submitted': submitted, 'horsedata': list})






def add_race(request):
    submitted = False
    if request.method =="POST":
        form = CreateRaceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_race?submitted=True')
    else:
        form = CreateRaceForm
        if 'submitted' in request.GET:
            submitted = True

    #list = horsedata.objects.all()

    return render(request, 'Race/add_race.html',{'form':form, 'submitted': submitted, 'Race': list})


def add_expense(request):
    submitted = False
    if request.method =="POST":
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return HttpResponseRedirect('/add_expense?submitted=True')
    else:
        form = CreateExpenseForm
        if 'submitted' in request.GET:
            submitted = True

    #list = expensedata.objects.all()

    return render(request, 'Expense/add_expense.html',{'form':form, 'submitted': submitted, 'Expense': list})

#Displays list of horses
def displayhorses(request):
    horses = Horse.objects.filter(user=request.user.id, sold=False )
    return render(request, 'Horse/Horses.html',
    {'horses': horses})
#Displays information for one horse
def displayHorse(request, horse_id):
    horse = Horse.objects.get(pk=horse_id)
    return render(request, 'Horse/display_horse.html',
    {'horse': horse})


def displayhorsesSold(request):
    horses = Horse.objects.filter(user=request.user.id, sold=True )
    return render(request, 'Horse/horses_sold.html',
    {'horses': horses})

def displayRace(request):
    race_list = Race.objects.all()

    myFilter = RaceFilter(request.GET, queryset=race_list)
    race_list = myFilter.qs

    return render(request, 'Race/display_race.html',
    {'race_list': race_list, 'myFilter': myFilter})

def displayExpense(request):
    expense_list = Expense.objects.all()

    myFilter = ExpenseFilter(request.GET, queryset=expense_list)
    expense_list = myFilter.qs

    return render(request, 'expense/display_expense.html',
    {'expense_list': expense_list,  'myFilter': myFilter})


def racePage(request):
    return render(request, 'Race/racePage.html', {})

def expensePage(request):
    return render(request, 'Expense/expensePage.html', {})


def home(request):
    return render(request, 'home/Home.html', {})


def edit(request, horse_id):
    horse = Horse.objects.get(pk=horse_id)
    form = CreateHorseForm(request.POST or None, instance = horse)
    if form.is_valid():
        form.save()
        return redirect('displayhorses')
    return render(request, 'Horse/edit.html', {'form': form, 'horse': horse})

def edit_race(request, race_id):
    race = Race.objects.get(pk=race_id)
    form = CreateRaceForm(request.POST or None, instance = race)
    if form.is_valid():
        form.save()
        return redirect('display_race')
    return render(request, 'race/edit_race.html', {'form': form, 'race': race})


def sell(request, horse_id):
    horse = Horse.objects.get(pk=horse_id)
    form = SellHorseForm(request.POST or None, instance = horse)
    if form.is_valid():
        form.save()
        return redirect('displayhorses')
    return render(request, 'Horse/edit.html', {'form': form, 'horse': horse})
