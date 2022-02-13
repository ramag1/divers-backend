from rest_framework import generics
# Create your views here.
from .models import Site, Log
# Import serializers
from .serializers import SiteSerializer, LogSerializer
from rest_framework import permissions
from divers.permissions import IsOwnerOrReadOnly

# api/sites/
# INDEX, POST
class SiteList(generics.ListCreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
# api/sites/id
# SHOW, PUT, DELETE
class SiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [IsOwnerOrReadOnly]
# api/log/
# INDEX, POST
class LogList(generics.ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
# api/log/id
# SHOW, PUT, DELETE
class LogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = [IsOwnerOrReadOnly]