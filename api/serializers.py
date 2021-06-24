from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Translation, Language
from typing import Dict


class TranslationSerializers(serializers.ModelSerializer):
    ''' Create TranslationSerializers '''

    class Meta:
        model = Translation
        fields = ['id',
                  'frontCard',
                  'backCard',
                  'target_language'
                  ]
        depth = 3

    def to_representation(
            self,
            instance) -> Dict[str, str]:
        ''' Modify representation a bit

        Returns
        -------
        Dict[str, str]
            a modified representation that will be displayed when called

        '''
        data = super().to_representation(instance)
        _id = data['id']
        frontCard = data['frontCard']
        backCard = data['backCard']
        target_language = data['target_language']
        updated_data = {'id': _id,
                        'frontCard': frontCard,
                        'backCard': backCard,
                        'target_language': target_language}
        return updated_data


class SingleTranslationSerializers(serializers.ModelSerializer):
    ''' SingleTranslationSerializers '''
    class Meta:
        model = Translation
        fields = ['id',
                  'frontCard',
                  'backCard',
                  'target_language']


class LanguageSerializers(serializers.ModelSerializer):
    ''' Create LanguageSerializers '''

    translations = TranslationSerializers(many=True, read_only=True)

    class Meta:
        model = Language
        fields = ['conversion',
                  'translations']
        depth = 3


class AvailableLanguagesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Language

        fields = ['conversion']

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     #     updated_data = {'language': data['conversion']}
    #     #     return updated_data
    #     # check the request is list view or detail view
    #     is_list_view = isinstance(self.instance, list)
    #     extra_ret = {'key': 'list value'} if is_list_view else {
    #         'key': 'single value'}
    #     data.update(extra_ret)
    #     return ret


class UserSerializer(serializers.HyperlinkedModelSerializer):
    ''' Create UserSerializer '''
    class Meta:
        model = User
        fields = ['url',
                  'username',
                  'email',
                  'is_staff']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    ''' Create GroupSerializer '''
    class Meta:
        model = Group
        fields = ['url',
                  'name']
