from django.db import models
# Create your models here.

class Vahaan(models.Model):
    Name = models.CharField(max_length=1080)
    contact = models.CharField(max_length=1080)
    DOB = models.CharField(max_length=1080)
    Class = models.CharField(max_length=1080)
    Address = models.CharField(max_length=1080)
    ApplicationNo = models.CharField(max_length=1080)
    EnrollmentNo = models.CharField(max_length=1080)
    LearningNo = models.CharField(max_length=1080)
    LicenseNo = models.CharField(max_length=1080)
    services = models.CharField(max_length=1000)
    Expiry = models.DateField()
    total = models.DecimalField(decimal_places=3,max_digits=120)
    Paid = models.DecimalField(decimal_places=3,max_digits=120)
    Remaining =  models.DecimalField(decimal_places=3,max_digits=120)
    systemDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Sarthi(models.Model):
    Name = models.CharField(max_length=1080)
    contact = models.CharField(max_length=1080)
    Address = models.CharField(max_length=1080)
    vehicleNo = models.CharField(max_length=1080)
    ClassId  = models.CharField(max_length=1080)
    InsuranceNo = models.CharField(max_length=1080)
    InsuranceStartDate = models.CharField(max_length=1080)
    InsuranceExpiryDate = models.CharField(max_length=1080)
    PUCNo = models.CharField(max_length=1080)
    PUCStartDate = models.CharField(max_length=1080)
    PUCExpiryDate = models.CharField(max_length=1080)
    FitnessNo = models.CharField(max_length=1080)
    FitnessStartDate = models.CharField(max_length=1080)
    FitnessExpiryDate = models.CharField(max_length=1080)
    PermitNo = models.CharField(max_length=1080)
    PermitStartDate = models.CharField(max_length=1080)
    PermitExpiryDate = models.CharField(max_length=1080)
    TaxNo = models.CharField(max_length=1080)
    TaxStartDate = models.CharField(max_length=1080)
    TaxExpiryDate = models.CharField(max_length=1080)
    GTNo = models.CharField(max_length=1080)
    GTStartDate = models.CharField(max_length=1080)
    GTExpiryDate = models.CharField(max_length=1080)
    PTNo = models.CharField(max_length=1080)
    PTStartDate = models.CharField(max_length=1080)
    PTExpiryDate = models.CharField(max_length=1080)
    services = models.CharField(max_length=1000)
    Expiry = models.DateField()
    total = models.DecimalField(decimal_places=3,max_digits=120)
    Paid = models.DecimalField(decimal_places=3,max_digits=120)
    Remaining =  models.DecimalField(decimal_places=3,max_digits=120)
    systemDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class VahaanClasses(models.Model):
    titleid = models.CharField(max_length=1080)
    title = models.CharField(max_length=1080)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class SarthiClasses(models.Model):
    titleid = models.CharField(max_length=1080)
    title = models.CharField(max_length=1080)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class VahaanServices(models.Model):
    titleid = models.CharField(max_length=1080)
    title = models.CharField(max_length=1080)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class SarthiServices(models.Model):
    titleid = models.CharField(max_length=1080)
    title = models.CharField(max_length=1080)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class VahaanServiesTracker(models.Model):
    VahaanId = models.CharField(max_length=1080)
    ServiceName  = models.CharField(max_length=1080,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return " VahaanId "+self.VahaanId


class SarthiServiesTracker(models.Model):
    SarthiId = models.CharField(max_length=1080)
    ServiceName  = models.CharField(max_length=1080,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return " Sarthi "+self.SarthiId