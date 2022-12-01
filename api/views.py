from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .models import Image, Gallery
from .serializers import ImageSerializer, GallerySerializer
from pymongo import MongoClient


def get_users_collection():
    url = "mongodb://localhost:27017/"

    client = MongoClient(url)
    db = client['galleryDB']
    return db['Users']


def get_picture_collection():
    url = "mongodb://localhost:27017/"

    client = MongoClient(url)
    db = client['galleryDB']
    return db['Pictures']


class UserList(GenericAPIView):

    collection = get_users_collection()

    def post(self, request, format=None):
        data = dict(request.data)
        self.collection.insert_one(data).inserted_id()
        return Response(data)

    def get(self, request, format=None):
        data = list(self.collection.find())
        data_clear = [{'first_name': row['first_name'], 'last_name': row['last_name']} for row in data]
        return Response(data_clear)


class HomeSite(GenericAPIView):
    def get(self, request, format=None):
        return Response({"message": "not implemented yet"})


class PictureList(GenericAPIView):

    collection = get_picture_collection()

    def post(self, request, format=None):
        data = dict(request.data)
        self.collection.insert_one(data)
        return Response({"message": "success"})

    def get(self, request, format=None):
        data = list(self.collection.find())
        data_clear = [{'name': row['name'], 'path': row['path'], 'size': row['size']} for row in data]
        return Response(data_clear)


class ImageList(GenericAPIView):

    serializer_class = ImageSerializer

    def get(self, request, format=None):
        image = Image.objects.all()
        serializer = ImageSerializer(image, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        image = ImageSerializer(data=request.data)
        if image.is_valid():
            image.save()
            return Response(image.data, status=status.HTTP_201_CREATED)
        return Response(image.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageDetail(GenericAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    serializer_class = ImageSerializer

    def get_object(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        image = self.get_object(pk)
        serializer = ImageSerializer(image)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        image = self.get_object(pk)
        serializer = ImageSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        image = self.get_object(pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GalleryList(GenericAPIView):

    serializer_class = GallerySerializer

    def get(self, request, format=None):
        gallery = Gallery.objects.all()
        serializer = GallerySerializer(gallery, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GalleryDetail(GenericAPIView):

    serializer_class = GallerySerializer

    def get_object(self, pk):
        try:
            return Gallery.objects.get(pk=pk)
        except Gallery.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        gallery = self.get_object(pk)
        serializer = GallerySerializer(gallery)
        gallery_id = serializer.data.get('id')
        images_in_gallery = list(Image.objects.filter(gallery=gallery_id).values())
        gallery_and_images = {'gallery_name': serializer.data['gallery_name'], 'images': images_in_gallery}
        return Response(gallery_and_images)

    def put(self, request, pk, format=None):
        gallery = self.get_object(pk)
        serializer = GallerySerializer(gallery, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



