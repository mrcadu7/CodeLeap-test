from rest_framework import viewsets
from .models import Careers
from .serializers import CareersSerializer

class CareersViewSet(viewsets.ModelViewSet):
    
    queryset = Careers.objects.all()
    serializer_class = CareersSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
