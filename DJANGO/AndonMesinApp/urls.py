from django.urls import path
from . import views

urlpatterns = [
path('mesin/register/', views.RegisterMesin.as_view(), name='register_mesin'),
path('', views.Dashboard.as_view(), name='view_dasboard'),
path('mesin/<int:pk>/update/', views.UpdateMesin.as_view(), name='update_mesin'),
path('mesin/<int:pk>/delete/', views.DeleteMesin.as_view(), name='delete_mesin'),
path('async-mesin/', views.AsyncMesin, name='async_mesin'),
]