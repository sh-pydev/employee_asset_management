from . models import *
from . serializers import *
from rest_framework import generics
from rest_framework import generics

#Available asset view.
class AssetList(generics.ListCreateAPIView):
    serializer_class = AssetSerializer
    
    def get_queryset(self):
        user = self.request.user
        return AssetType.objects.filter(company=user)
    
    def perform_create(self, serializer):
        serializer.save(company = self.request.user)

class AssetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AssetType.objects.all()
    serializer_class = AssetSerializer

    def get_queryset(self):
        user = self.request.user
        return AssetType.objects.filter(company=user)

    def perform_update(self, serializer):
        serializer.save(company = self.request.user)

#Available employe view.
class EmployeeList(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        user = self.request.user
        return Employee.objects.filter(company=user)

    def perform_create(self, serializer):
        serializer.save(company = self.request.user)

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Employee.objects.filter(company=user)
    
    def perform_update(self, serializer):
        serializer.save(company = self.request.user)
        
#Given asset view.  
class GivenAssetList(generics.ListCreateAPIView):
    serializer_class = GivenAssetSerializer
    
    def get_queryset(self):
        user = self.request.user
        return GivenAsset.objects.filter(given_to__company=user)
    
class GivenAssetDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GivenAssetSerializer
    
    def get_queryset(self):
        user = self.request.user
        return GivenAsset.objects.filter(given_to__company=user)