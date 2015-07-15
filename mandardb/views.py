from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from mandardb.serializers import *
# Create your views here.

class AddressCreate(APIView):
    """
    List a snippet, or create a new snippet.
    """
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            raise Http404

    def get(self, request, address_id, format=None):
        address = self.get_object(address_id)
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def put(self, request, address_id, format=None):
        address = self.get_object(address_id)
        serializer = AddressSerializer(address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            addressObj = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressGet(APIView):
    """
    List all snippets
    """
    def get(self, request, format=None):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses,many=True)
        return Response(serializer.data)

class PersonCreate(APIView):
    """
    List a snippet, or create a new snippet.
    """
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, person_id, format=None):
        person = self.get_object(person_id)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def put(self, request, person_id, format=None):
        person = self.get_object(person_id)
        serializer = PersonSerializer(person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            personObj = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonGet(APIView):
    """
    List all snippets
    """
    def get(self, request, format=None):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons,many=True)
        return Response(serializer.data)

class FeedCreate(APIView):
    """
    List a snippet, or create a new snippet.
    """
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get_object(self, pk):
        try:
            return Feed.objects.get(pk=pk)
        except Feed.DoesNotExist:
            raise Http404

    def get(self, request, feed_id, format=None):
        feed = self.get_object(feed_id)
        serializer = FeedSerializer(feed)
        return Response(serializer.data)

    def put(self, request, feed_id, format=None):
        feed = self.get_object(feed_id)
        serializer = FeedSerializer(feed, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = FeedSerializer(data=request.data)
        if serializer.is_valid():
            feedObj = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FeedGet(APIView):
    """
    List all snippets
    """
    def get(self, request, format=None):
        feeds = Feed.objects.all()
        serializer = FeedSerializer(feeds,many=True)
        return Response(serializer.data)

class ImageUpload(APIView):
    """
    Upload an image
    """
    def get_object(self, pk):
        try:
            return Images.objects.get(pk=pk)
        except Images.DoesNotExist:
            raise Http404

    def get(self, request, image_id, format=None):
        image = self.get_object(image_id)
        serializer = ImageSerializer(image)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            imageObj = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
