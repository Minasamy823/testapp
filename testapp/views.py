from django.shortcuts import get_object_or_404
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
import random
import string


def generate_key(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


class TestView(APIView):

    def get(self, request):
        models = TestModel.objects.all()
        serializer = TestSerializer(models, many=True)
        return Response(serializer.data)

    def post(self, request):
        key = generate_key(40)
        name = request.data.get('name')
        data = [{"name": name, 'key': key}]
        serializer = TestSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('invalid info')


class TestDetails(generics.RetrieveUpdateAPIView, mixins.DestroyModelMixin):
    serializer_class = TestSerializer

    def get_object(self):
        id_ = self.kwargs["id"]
        obj = get_object_or_404(TestModel, pk=id_)
        return obj

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        name = request.data.get('name')
        key = generate_key(40)
        data = {"name": name, 'key': key}
        serializer = TestSerializer(data=data, instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('NOt valid')

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
