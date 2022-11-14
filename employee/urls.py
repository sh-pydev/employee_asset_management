from django.urls import path
from . views import *

urlpatterns = [
    path('asset/', AssetList.as_view(), name='ListOfAssets'),
    path('asset/<int:pk>', AssetDetail.as_view(), name='IndividualAsset'),
    
    path('employee/', EmployeeList.as_view(), name='ListOfEmployees'),
    path('employee/<int:pk>', EmployeeDetail.as_view(), name='IndividualEmployee'),
    
    path('given_asset/', GivenAssetList.as_view(), name='AssetsGiven'),
    path('given_asset/<int:pk>', GivenAssetDetail.as_view(), name='AssetDetail'),
]
