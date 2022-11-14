from . models import *
from knox.auth import TokenAuthentication
from . serializers import *
from rest_framework import generics, filters, permissions

#Available asset view.
class AssetList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AssetSerializer
    
    def get_queryset(self):
        user = self.request.user
        return AssetType.objects.filter(company=user)
    
    def perform_create(self, serializer):
        serializer.save(company = self.request.user)

class AssetDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AssetSerializer

    def get_queryset(self):
        user = self.request.user
        return AssetType.objects.filter(company=user)

    def perform_update(self, serializer):
        serializer.save(company = self.request.user)

#Available employe view.
class EmployeeList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        user = self.request.user
        return Employee.objects.filter(company=user)

    def perform_create(self, serializer):
        serializer.save(company = self.request.user)

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeeSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Employee.objects.filter(company=user)
    
    def perform_update(self, serializer):
        serializer.save(company = self.request.user)
        
#Given asset view.  
class GivenAssetList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['given_to__employee_id',]
    serializer_class = GivenAssetSerializer
    
    def get_queryset(self):
        user = self.request.user
        return GivenAsset.objects.filter(given_to__company=user)
    
class GivenAssetDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GivenAssetSerializer
    
    def get_queryset(self):
        user = self.request.user
        return GivenAsset.objects.filter(given_to__company=user)