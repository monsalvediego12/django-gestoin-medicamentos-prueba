from gest_prueba.models import Medicamentos, Tratamientos, Enfermedades
from gest_prueba.serializers import (
    MedicamentosSerializer,
    TratamientosSerializer,
    EnfermedadesSerializer,
)
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import F, Count


class MedicamentosViewSet(viewsets.ModelViewSet):

    queryset = Medicamentos.objects.all()
    serializer_class = MedicamentosSerializer
    permission_classes = []


class TratamientosViewSet(viewsets.ModelViewSet):

    queryset = Tratamientos.objects.all()
    serializer_class = TratamientosSerializer
    permission_classes = []


class EnfermedadesViewSet(viewsets.ModelViewSet):

    queryset = Enfermedades.objects.all()
    serializer_class = EnfermedadesSerializer
    permission_classes = []


class QuerysViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    def s1(self, request):
        res = {
            "title": "Obtener la lista de todas las enfermedades que tengan más de 6 medicamentos diferentes indicados para su tratamiento.",
            "items": [],
        }
        queryset = (
            Enfermedades.objects.annotate(
                num_medicamentos=Count("tratamientos__medicamentos", distinct=True)
            )
            .filter(num_medicamentos__gt=6)
            .distinct()
        )
        res["items"] = normalizeQuerysetJson(queryset)
        return Response(res)

    def s2(self, request):
        res = {
            "title": "Obtener la lista de todas las enfermedades que tengan entre 7 y 12 medicamentos diferentes indicados y cuenten con al menos 3 tratamientos posibles.",
            "items": [],
        }
        queryset = Enfermedades.objects.annotate(
            num_tratamientos=Count(
                "tratamientos", distinct=True
            ),  # Contar tratamientos distintos
            num_medicamentos=Count(
                "tratamientos__medicamentos", distinct=True
            ),  # Contar medicamentos distintos
        ).filter(
            num_tratamientos__gte=3,  # Al menos 3 tratamientos
            num_medicamentos__gte=7,  # Al menos 7 medicamentos
            num_medicamentos__lte=12,  # No más de 12 medicamentos
        )
        res["items"] = normalizeQuerysetJson(queryset)
        return Response(res)

    def s3(self, request):
        res = {
            "title": "Obtener la lista de medicamentos que estén indicados en el tratamiento de menos de 2 enfermedades.",
            "items": [],
        }

        queryset = Medicamentos.objects.annotate(
            num_enfermedades=Count(
                "trat_medicamento__enfermedad_tratamiento", distinct=True
            )
        ).filter(num_enfermedades__lt=2)

        res["items"] = normalizeQuerysetJson(queryset)

        return Response(res)

    def s4(self, request):
        res = {
            "title": "Mostrar la cantidad de tratamientos y medicamentos diferentes indicados a cada enfermedad, presentando al menos el nombre de la enfermedad y los valores solicitados.",
            "items": [],
        }

        # Anotamos cada enfermedad con la cantidad de tratamientos y medicamentos distintos
        queryset = Enfermedades.objects.annotate(
            cantidad_tratamientos=Count("tratamientos", distinct=True),
            cantidad_medicamentos=Count("tratamientos__medicamentos", distinct=True),
        )

        for item in queryset:
            dataItem = {
                "nombre": item.name,
                "cantidad_tratamientos": item.cantidad_tratamientos,
                "cantidad_medicamentos": item.cantidad_medicamentos,
            }

            res["items"].append(dataItem)

        return Response(res)


def normalizeQuerysetJson(queryset):
    data = []
    try:
        if queryset.exists():
            for item in queryset:
                data.append({"id": item.id, "name": item.name})
    except:
        pass
    return data
