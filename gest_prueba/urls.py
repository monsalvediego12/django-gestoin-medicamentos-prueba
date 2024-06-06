from django.urls import include, path
from rest_framework import routers
from gest_prueba.views import MedicamentosViewSet, EnfermedadesViewSet, TratamientosViewSet, QuerysViewSet

# from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'medicamentos', MedicamentosViewSet)
router.register(r'enfermedades', EnfermedadesViewSet)
router.register(r'tratamientos', TratamientosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('q_1/', QuerysViewSet.as_view({'get': 's1'})),
    path('q_2/', QuerysViewSet.as_view({'get': 's2'})),
    path('q_3/', QuerysViewSet.as_view({'get': 's3'})),
    path('q_4/', QuerysViewSet.as_view({'get': 's4'})),
]