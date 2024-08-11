from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validation import cpf_invalido, nome_invalido, celular_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante #modelo
        fields = ['id','nome','email','cpf', 'data_nascimento', 'celular'] #campos

    def validate(self,dados):
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve ter um valor válido!'})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome só pode ter letras'})
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'celular':'O celular precisa seguir o modelo: 86 99999-9999 (respeitando os traços e espaços)'})
        return dados
           
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
        
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = [] #informa que não quero excluir nenhum campo, ou seja, terá todos os campos

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer): #lista matriculas por estudante
    curso = serializers.ReadOnlyField(source='curso.descricao') #campo somente para leitura 
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula 
        fields = ['curso','periodo']    

    def get_periodo(self,obj): #default
        return obj.get_periodo_display() #captura um valor e retorna
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer): #lista matricula por curso
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']

class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante #modelo
        fields = ['id','nome','email','celular'] #campos