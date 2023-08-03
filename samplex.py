from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . models import MyModel
from . serializers import MyModelSerializer

class MyModelListCreateView(ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

class MyModelRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
