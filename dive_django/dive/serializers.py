from rest_framework import serializers
from .models import Site, Visitor


class SiteSerializer(serializers.HyperlinkedModelSerializer):
    visitors = serializers.HyperlinkedRelatedField(
        view_name='visitor_detail', many=True, read_only=True)

    site_url = serializers.ModelSerializer.serializer_url_field(view_name='site_detail')

    class Meta:
        model = Site
        fields = ('id', 'name', 'country', 'max_depth', 'site_type', 'marine_life' , 'visitors', 'site_url')

class VisitorSerializer(serializers.HyperlinkedModelSerializer):
    site = serializers.HyperlinkedRelatedField(
        view_name='site_detail', read_only=True)

    site_id = serializers.PrimaryKeyRelatedField(
        queryset = Site.objects.all(),
        source = 'site'
    )

    class Meta:
        model = Visitor
        fields = ('id', 'name', 'site', 'visited', 'site_id', 'favorite', 'bucket_list')