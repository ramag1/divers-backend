from rest_framework import generics
# Create your views here.
from .models import Site, Visitor
# Import serializers
from .serializers import SiteSerializer, VisitorSerializer


# api/sites/
# INDEX, POST
class SiteList(generics.ListCreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

# api/sites/id
# SHOW, PUT, DELETE
class SiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

# api/visitor/
# INDEX, POST
class VisitorList(generics.ListCreateAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer

# api/visitor/id
# SHOW, PUT, DELETE
class VisitorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
