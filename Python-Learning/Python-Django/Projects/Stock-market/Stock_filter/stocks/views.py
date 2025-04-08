from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Stock, TopSector
from .serializers import StockSerializer, TopSectorSerializer
from django.db import models
from rest_framework.decorators import action
from rest_framework.views import APIView
from .services import NseService

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    
    @action(detail=False, methods=['get'])
    def filtered_stocks(self, request):
        threshold = float(request.query_params.get('threshold', 0.3))
        sectors = request.query_params.get('sectors', '')
        
        queryset = Stock.objects.filter(
            current_price__gte=models.F('high_52w') * (1 - threshold)
        )
        
        if sectors:
            queryset = queryset.filter(sector__in=sectors.split(','))
            
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class TopSectorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TopSector.objects.all()
    serializer_class = TopSectorSerializer

class NseUpdateView(APIView):
    def post(self, request):
        service = NseService()
        service.update_stock_data()
        return Response({"status": "data updated"}, status=status.HTTP_200_OK)