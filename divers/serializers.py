from rest_framework import serializers
from .models import Site, Log

class LogSerializer(serializers.HyperlinkedModelSerializer):
    site_id = serializers.PrimaryKeyRelatedField(
        queryset = Site.objects.all(),
        source = 'site'
    )

    site = serializers.HyperlinkedRelatedField(
        view_name='site_detail', read_only=True)
    
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Log
        fields = ('id', 'site', 'visited', 'site_id', 'favorite', 'bucket_list', 'owner')

class SiteSerializer(serializers.HyperlinkedModelSerializer):
    logs = serializers.HyperlinkedRelatedField(
        view_name='log_detail', many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Site
        fields = ('id', 'name', 'country', 'max_depth', 'site_type', 'marine_life' , 'logs', 'owner')
