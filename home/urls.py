from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import horse.views
from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name = "home"),
path('add_horse', views.add_horse, name="add-horse"),
path('add_race', views.add_race, name="add-race"),
path('add_expense', views.add_expense, name="add-expense"),

path('Horses', views.displayhorses, name="displayhorses"),
path('horses_sold', views.displayhorsesSold, name="displayhorsesSold"),
path('sell/<horse_id>', views.sell, name='sell'),
path('edit/<horse_id>', views.edit, name='edit'),
path('displayHorse/<horse_id>', views.displayHorse, name='displayHorse'),


path('racePage', views.racePage,name="racePage"),
path('edit_race/<race_id>', views.edit_race, name='edit_race'),
path('display_race', views.displayRace, name="display_race"),

path('expensePage', views.expensePage,name="expensePage"),
path('display_expense', views.displayExpense, name = "display_expense"),
]
