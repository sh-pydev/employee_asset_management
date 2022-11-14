from django.db import models
from django.contrib.auth.models import User


primary_asset_condition = [
    ['1', 'New'],
    ['2', 'Old but usable'],
    ['3', 'Not given yet']
]

#probable asset conditions are summerized here. If necessary, this can also be converted into a select type field

secondary_asset_condition = [
    ['1', 'New'],
    ['2', 'Old but usable'],
    ['3', 'Old and not usable'],
    ['4', 'Broken'],
    ['5', 'Not returned yet'],
    ['6', 'Not given yet']
]

class AssetType(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE, null = True) #The owner/responsible person of a company should have an account as a user.
    name = models.CharField(max_length=50, null=True, blank=False) #What kind of asset is this.
    
    #Two different company may have the same genre. Say, laptop. But One different company can not update one asset genre more than once. The meta class is used for this.
    class Meta:
        constraints = [models.UniqueConstraint(fields=['company', 'name'], name = 'unique')]
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    employee_id = models.IntegerField(null=True, blank=False, unique=True)
    #One unique ID for each employee to distinguish them out. To make search option workable, it is necessary.
    employee_name = models.CharField(max_length=100, blank=False)
    company = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return str(self.employee_id)
    
class GivenAsset(models.Model):
    asset = models.ForeignKey(AssetType, on_delete=models.CASCADE, null = True)
    given_to = models.ForeignKey(Employee, on_delete=models.CASCADE, null = True)
    given_asset_status = models.CharField(max_length=20, choices=primary_asset_condition, default='3')
    asset_given_at = models.DateField(null=True, blank=True)
    returned_asset_status = models.CharField(max_length=20, choices=secondary_asset_condition, default='6')
    asset_returned_at = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.asset