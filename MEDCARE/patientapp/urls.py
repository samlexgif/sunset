from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_reading/', views.add_reading, name='add_reading'),
    path('resources/', views.resource_list, name='resource_list'),
    path('resources/<int:resource_id>/', views.resource_detail, name='resource_detail'),
    path('mealplan/',views.Nutrionalfacts,name='add_meal_plan'),

]


