
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('listar_riesgo', views.listar_riesgo, name="listar_riesgo"),
    path('load/', views.load_data),
    path('listarriesgos/', views.get_list, name="listarriesgo"),
]
