from rest_framework import serializers

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            # write_only só na hora do cadastro apresentar o email
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )


class CursoSerializer(serializers.ModelSerializer):
    """# Nested Relationship, mostra as avaliações para leitura no curso
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    """

    """
    # HyperLiked Related field, mostra link de todas avaliações
    avaliacoes = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='avaliacao-detail')
    """

    # Primary key Related Field, mostra o id de todas avaliações
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )
