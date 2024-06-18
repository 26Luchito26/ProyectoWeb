from django.urls import path
from . import views

urlpatterns = [
    path('solicitudes_retiro/', views.solicitudes_retiro, name="Solicitudes_Retiro"),
    path('solicitudes_material/', views.solicitudes_material, name="Solicitudes_Material"),
    path('solicitudes_epps/', views.solicitudes_epps, name="Solicitudes_Epps"),
    path('exportar_solicitudes_csv/', views.exportar_solicitudes_excel, name="exportar_solicitudes_excel"),
]