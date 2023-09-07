# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from . models import MyModel
# from . serializers import MyModelSerializer

# class MyModelListCreateView(ListCreateAPIView):
#     queryset = MyModel.objects.all()
#     serializer_class = MyModelSerializer

# class MyModelRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     queryset = MyModel.objects.all()
#     serializer_class = MyModelSerializer






# samples with python language >>>>>>>>>>>>>>>>>>>

# string method
message = "Hello, world!"
length = len(message)
uppercase_message = message.upper()
print(uppercase_message)
print(type(uppercase_message))

#try and 
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")

# file handiling  
with open("data.txt", "r") as file:
    content = file.read()
with open("output.txt", "w") as file:
    file.write("Hello, file!")
    