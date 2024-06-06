from gest_prueba.models import Medicamentos, Tratamientos, Enfermedades

from rest_framework import serializers


class MedicamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamentos
        fields =  '__all__'



class TratamientosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamientos
        fields =  '__all__'



class EnfermedadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermedades
        fields =  '__all__'


