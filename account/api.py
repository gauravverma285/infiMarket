from rest_framework.views import APIView
from rest_framework.response import Response
from account.serializers import *
from rest_framework import status

class CategoryAPIViews(APIView):
    def post(self, request):
        res={}
        serializer=categorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            res['status']=True
            res['message']="add the caytegory"
            res['data']=serializer.data
            return Response(res, status=status.HTTP_201_CREATED)
        else:
            res['status'] = False
            res['message'] = 'Failed to create '
            res['errors'] = serializer.errors
            return Response(res, status=status.HTTP_400_BAD_REQUEST)


class ProductAPIViews(APIView):
    def get(self,request):
        res={}
        products=Product.objects.all()
        serializer = productSerializer(products,many=True)
        res['status']=True
        res['message']="add the product"
        res['data']=serializer.data
        return Response(res, status=status.HTTP_200_OK)

    def post(self, request):
        res={}
        serializer=productSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            res['status']=True
            res['message']="add the product"
            res['data']=serializer.data
            return Response(res, status=status.HTTP_201_CREATED)
        else:
            res['status'] = False
            res['message'] = 'Failed to create '
            res['errors'] = serializer.errors
            return Response(res, status=status.HTTP_400_BAD_REQUEST)