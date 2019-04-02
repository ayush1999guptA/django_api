
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.response import Response
from .serializers import StockSerializers
from .models import Stock
from rest_framework.views import APIView
from rest_framework import status

class StockList(APIView):

    def get(self, request):

        stock = Stock.objects.all()

        serializer = StockSerializers(stock,many=True)

        return Response(serializer.data)


    def post(self, request):
        serializer = StockSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        ticker=request.data
        tick=ticker['ticker']
        stock=Stock.objects.get(pk=tick)
        serializer=StockSerializers(instance=stock,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        ticker = request.data
        tick = ticker['ticker']
        stock = Stock.objects.get(pk=tick)
        stock.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
