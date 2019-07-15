from rest_framework import serializers
from djangoRestTutorial.main.models import Study


class StudySerializer(serializers.Serializer):

    class Meta:
        model = Study
        fields = ('name', 'code')
    #
    # def create(self, validated_data):
    #     """
    #     Create new Study instance
    #     :param validated_data:
    #     :return:
    #     """
    #     return Study.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update Study instance
    #     :param instance:
    #     :param validated_data:
    #     :return:
    #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.save()
    #     return instance
