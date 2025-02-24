from rest_framework import serializers

from pacientes.models import Pacientes
from agendamentos.api.serializers import AgendamentosDetalhesSerializer

class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'

class PacientesDetalhesSerializer(serializers.ModelSerializer):
    agendamentos = AgendamentosDetalhesSerializer(many=True, read_only=True)

    class Meta:
        model = Pacientes
        fields = [
            'id_paciente', 
            'nome', 
            'data_nascimento', 
            'endereco', 
            'num_endereco', 
            'bairro_endereço', 
            'cep', 
            'data_cadastro', 
            'rg', 
            'agendamentos'
        ]
    