
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin
'''#get
@api_view(['GET'])
def stores(request):
    k=Product.objects.all()
    serial=productserializer(k,many=True)
    return Response({'status':200,'payload':serial.data})'''

class products(GenericAPIView,ListModelMixin):
    queryset=Product.objects.all()
    serializer_class = productserializer
    def get(self,request):
        return self.list(request)

'''#create
@api_view(['POST'])
def post_product(request):
    k = Product.objects.all()
    serial = productserializer(data=request.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)'''
class create_prod(GenericAPIView,CreateModelMixin):
    queryset=Product.objects.all()
    serializer_class = productserializer
    def post(self,request):
        return self.create(request)

class ret_prod(GenericAPIView,RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = productserializer
    def get(self, request,**kwargs):
        return self.retrieve(request,**kwargs)
#update
'''@api_view(['POST'])
def update_product(request,id):
    k = Product.objects.get(id=id)
    serial = productserializer(instance=k,data=request.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)'''
class update_product(GenericAPIView,UpdateModelMixin):
    queryset = Product.objects.all()
    serializer_class = productserializer
    def put(self, request,**kwargs):
        return self.update(request,**kwargs)


#delete
@api_view(['DELETE'])
def del_product(request,id):
    k = Product.objects.get(id=id)
    k.delete()
    return Response('Product is deleted')


