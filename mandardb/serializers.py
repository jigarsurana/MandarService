from rest_framework import serializers
from models import *

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('line1', 'line2', 'city', 'zipcode', 'state', 'country')

    def create(self, validated_data):
        return Address.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.line1 = validated_data.get('line1', instance.line1)
        instance.line2 = validated_data.get('line2', instance.line2)
        instance.city = validated_data.get('city', instance.city)
        instance.zipcode = validated_data.get('zipcode', instance.zipcode)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance


class PersonSerializer(serializers.Serializer):
    person_id = serializers.CharField(read_only=True)
    home_address = AddressSerializer(required=False)
    office_address = AddressSerializer(required=False)
    first_name = serializers.CharField(max_length=None,required=False)
    middle_name = serializers.CharField(max_length=None,required=False)
    last_name = serializers.CharField(max_length=None,required=False)
    mobile1 = serializers.RegexField(regex=r'[0-9]+',required=False)
    mobile2 = serializers.RegexField(regex=r'[0-9]+',required=False)
    landline1 = serializers.RegexField(regex=r'[0-9]+',required=False)
    landline2 = serializers.RegexField(regex=r'[0-9]+',required=False)
    office1 = serializers.RegexField(regex=r'[0-9]+',required=False)
    office2 = serializers.RegexField(regex=r'[0-9]+',required=False)

    def create(self, validated_data):
        h_address = validated_data.pop('home_address')
        hAddressObj = Address.objects.create(**h_address)
        validated_data['home_address'] = hAddressObj

        o_address = validated_data.pop('office_address')
        oAddressObj = Address.objects.create(**o_address)
        validated_data['office_address'] = oAddressObj

        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        h_address = validated_data.pop('home_address')
        if (h_address.get('line1') is not None and h_address.get('city') is not None and h_address.get('state') is not None):
            hAddressObj = Address.objects.create(**h_address)
            instance.home_address = hAddressObj
        o_address = validated_data.pop('office_address')
        if (o_address.get('line1') is not None and o_address.get('city') is not None and o_address.get('state') is not None):
            hAddressObj = Address.objects.create(**o_address)
            instance.office_address = hAddressObj
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.middle_name = validated_data.get('middle_name', instance.middle_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.mobile1 = validated_data.get('mobile1', instance.mobile1)
        instance.mobile2 = validated_data.get('mobile2', instance.mobile2)
        instance.landline1 = validated_data.get('landline1', instance.landline1)
        instance.landline2 = validated_data.get('landline2', instance.landline2)
        instance.office1 = validated_data.get('office1', instance.office1)
        instance.office2 = validated_data.get('office2', instance.office2)
        instance.save()
        return instance

class FeedSerializer(serializers.Serializer):
    feed_id = serializers.CharField(read_only=True)
    feed_title = serializers.CharField()
    feed_text = serializers.CharField()
    feed_image = serializers.URLField(max_length=200, min_length=None, allow_blank=True)
    upload_date = serializers.DateTimeField()
    uploaded_by = serializers.CharField()

    def create(self, validated_data):
        return Feed.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.feed_title = validated_data.get('feed_title', instance.feed_title)
        instance.feed_text = validated_data.get('feed_text', instance.feed_text)
        instance.feed_image = validated_data.get('feed_image', instance.feed_image)
        instance.upload_date = validated_data.get('upload_date', instance.upload_date)
        instance.uploaded_by = validated_data.get('uploaded_by', instance.uploaded_by)

class ImageSerializer(serializers.Serializer):
    img = serializers.ImageField(use_url=True)
    image_id = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Images.objects.create(**validated_data)
