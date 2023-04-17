from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class PlanViewSet(ModelViewSet):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()

    def get(self, request):
        search = request.query_params.get('search', None)
        queryset = Plan.objects.all()
        if search:
            queryset = queryset.filter(sarlavha__icontains=search)
        serializer = PlanSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
