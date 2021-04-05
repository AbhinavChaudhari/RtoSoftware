from django.shortcuts import render,redirect
from .models import Vahaan,VahaanClasses,VahaanServices,VahaanServiesTracker,Sarthi,SarthiServices,SarthiClasses,SarthiServiesTracker
from datetime import datetime
from django.db.models import Q,Sum
import csv
from django.http import HttpResponse
# pdf
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
import os





# Create your views here.
def index(request):
    return render(request,'RTOMod/index.html')

def vahaan(request):
    AllVhn = Vahaan.objects.all()
    return render(request, 'RTOMod/vahaan.html',{'AllVhn':AllVhn})

def vahaanRegister(request):
    if request.method == 'POST':
        if 'vahaanRegister' in request.POST:
            vhn = Vahaan()
            vhn.Name = request.POST['name']
            vhn.systemDate = datetime.today().strftime('%Y-%m-%d')
            vhn.contact = request.POST['contact']
            vhn.DOB = request.POST['dob']
            vhn.Class = request.POST['classid']
            vhn.Address = request.POST['address']
            vhn.ApplicationNo = request.POST['applicationNO']
            vhn.EnrollmentNo = request.POST['enrollmentNO']
            vhn.LearningNo = request.POST['learningNO']
            vhn.LicenseNo = request.POST['licenseNO']
            vhn.total = request.POST['total']
            vhn.Paid = request.POST['amtPaid']
            vhn.Remaining = request.POST['remaining']
            vhn.services = request.POST.getlist('myservice')
            vhn.Expiry = request.POST['serviceExpiryDate']

            vhn.save()

            AllServices = request.POST.getlist('myservice')
            for service in AllServices:
                VS = VahaanServiesTracker()
                VS.VahaanId = vhn.id
                VS.ServiceName = service
                VS.save()
            return redirect('RTOModVahaan')
            print(AllServices)
    else:
        vhnClasses = VahaanClasses.objects.all()
        vhnServices = VahaanServices.objects.all()
        return render(request, 'RTOMod/vahaanRegister.html',{'vhnClasses':vhnClasses,'vhnServices':vhnServices})

def vahaanEdit(request, id):
    vhn = Vahaan.objects.get(pk=id)
    if request.method == 'POST':
        if 'vahaanUpdate' in request.POST:
            vhn.Name = request.POST['name']
            vhn.contact = request.POST['contact']
            vhn.DOB = request.POST['dob']
            vhn.Class = request.POST['classid']
            vhn.Address = request.POST['address']
            vhn.ApplicationNo = request.POST['applicationNO']
            vhn.EnrollmentNo = request.POST['enrollmentNO']
            vhn.LearningNo = request.POST['learningNO']
            vhn.LicenseNo = request.POST['licenseNO']
            vhn.total = request.POST['total']
            vhn.Paid = request.POST['paid']
            vhn.Remaining = request.POST['remaining']
            vhn.save()
            AllServices = request.POST.getlist('myservice')
            VahaanServiesTracker.objects.filter(VahaanId = id).delete()
            for service in AllServices:
                VS = VahaanServiesTracker()
                VS.VahaanId = id
                VS.ServiceName = service
                VS.save()
            return redirect('RTOModVahaan')
    else:
        vhnClasses = VahaanClasses.objects.all()
        vhnServices = VahaanServices.objects.all()
        RawVSTs = VahaanServiesTracker.objects.filter(VahaanId=id).values_list('ServiceName', flat=True)
        VSTs = list(RawVSTs)
        return render(request,'RTOMod/vahaanEdit.html',{'vhn':vhn,'vhnClasses':vhnClasses,'vhnServices':vhnServices,'VSTs':VSTs})

def vahaanView(request, id):
    vhn = Vahaan.objects.get(pk=id)
    vhnClasses = VahaanClasses.objects.all()
    vhnServices = VahaanServices.objects.all()
    RawVSTs = VahaanServiesTracker.objects.filter(VahaanId=id).values_list('ServiceName', flat=True)
    VSTs = list(RawVSTs)
    return render(request,'RTOMod/vahaanView.html',{'vhn':vhn,'vhnClasses':vhnClasses,'vhnServices':vhnServices,'VSTs':VSTs})

def vahaanDelete(request, id):
    vhn = Vahaan.objects.get(pk=id)
    if request.method == 'POST':
        if 'vahaanDelete' in request.POST:
            vhn.delete()
            return redirect('RTOModVahaan')
    else:
        vhnClasses = VahaanClasses.objects.all()
        RawVSTs = VahaanServiesTracker.objects.filter(VahaanId=id).values_list('ServiceName', flat=True)
        vhnServices = VahaanServices.objects.all()
        VSTs = list(RawVSTs)
        return render(request,'RTOMod/vahaanDelete.html',{'vhn':vhn,'vhnClasses':vhnClasses,'vhnServices':vhnServices,'VSTs':VSTs})

def sarthi(request):
    AllSAR = Sarthi.objects.all()
    return render(request, 'RTOMod/sarthi.html',{'AllSAR':AllSAR})

def sarthiRegister(request):
    if request.method == 'POST':
        if 'SarthiRegister' in request.POST:
            SAR = Sarthi()
            SAR.Name = request.POST['Name']
            SAR.contact = request.POST['Contact']
            SAR.systemDate = datetime.today().strftime('%Y-%m-%d')
            SAR.Address = request.POST['Address']
            SAR.vehicleNo = request.POST['VehicleNo']
            SAR.ClassId = request.POST['ClassID']
            SAR.InsuranceNo = request.POST['InsuranceNo']
            SAR.InsuranceStartDate = request.POST['InsuranceStartDate']
            SAR.InsuranceExpiryDate = request.POST['InsuranceExpiryDate']
            SAR.PUCNo = request.POST['PUCNo']
            SAR.PUCStartDate = request.POST['PUCStartDate']
            SAR.PUCExpiryDate = request.POST['PUCExpiryDate']
            SAR.FitnessNo = request.POST['FitnessNo']
            SAR.FitnessStartDate = request.POST['FitnessStartDate']
            SAR.FitnessExpiryDate = request.POST['FitnessExpiryDate']
            SAR.PermitNo = request.POST['PermitNo']
            SAR.PermitStartDate = request.POST['PermitStartDate']
            SAR.PermitExpiryDate = request.POST['PermitExpiryDate']
            SAR.TaxNo = request.POST['TaxNo']
            SAR.TaxStartDate = request.POST['TaxStartDate']
            SAR.TaxExpiryDate = request.POST['TaxExpiryDate']
            SAR.GTNo = request.POST['GTNo']
            SAR.GTStartDate = request.POST['GTStartDate']
            SAR.GTExpiryDate = request.POST['GTExpiryDate']
            SAR.PTNo = request.POST['PTNo']
            SAR.PTStartDate = request.POST['PTStartDate']
            SAR.PTExpiryDate = request.POST['PTExpiryDate']
            SAR.total = request.POST['total']
            SAR.Paid = request.POST['amtPaid']
            SAR.Remaining = request.POST['amtRemaining']
            SAR.services = request.POST.getlist('myservice')
            SAR.Expiry = request.POST['serviceExpiryDate']
            SAR.save()
            AllSarthiServices = request.POST.getlist('myservice')
            for service in AllSarthiServices:
                SST = SarthiServiesTracker()
                SST.SarthiId = SAR.id
                SST.ServiceName = service
                SST.save()
            return redirect('RTOModSarthi')

    else:
        SARClasses = SarthiClasses.objects.all()
        SARServices = SarthiServices.objects.all()
        return render(request, 'RTOMod/sarthiRegister.html',{'SARClasses':SARClasses,'SARServices':SARServices})

def sarthiEdit(request,id):
    SAR = Sarthi.objects.get(pk=id)
    if request.method == 'POST':
        if 'SarthiUpdate' in request.POST:
            SAR.Name = request.POST['Name']
            SAR.contact = request.POST['Contact']
            SAR.Address = request.POST['Address']
            SAR.vehicleNo = request.POST['VehicleNo']
            SAR.ClassId = request.POST['classid']
            SAR.InsuranceNo = request.POST['InsuranceNo']
            SAR.InsuranceStartDate = request.POST['InsuranceStartDate']
            SAR.InsuranceExpiryDate = request.POST['InsuranceExpiryDate']
            SAR.PUCNo = request.POST['PUCNo']
            SAR.PUCStartDate = request.POST['PUCStartDate']
            SAR.PUCExpiryDate = request.POST['PUCExpiryDate']
            SAR.FitnessNo = request.POST['FitnessNo']
            SAR.FitnessStartDate = request.POST['FitnessStartDate']
            SAR.FitnessExpiryDate = request.POST['FitnessExpiryDate']
            SAR.PermitNo = request.POST['PermitNo']
            SAR.PermitStartDate = request.POST['PermitStartDate']
            SAR.PermitExpiryDate = request.POST['PermitExpiryDate']
            SAR.TaxNo = request.POST['TaxNo']
            SAR.TaxStartDate = request.POST['TaxStartDate']
            SAR.TaxExpiryDate = request.POST['TaxExpiryDate']
            SAR.GTNo = request.POST['GTNo']
            SAR.GTStartDate = request.POST['GTStartDate']
            SAR.GTExpiryDate = request.POST['GTExpiryDate']
            SAR.PTNo = request.POST['PTNo']
            SAR.PTStartDate = request.POST['PTStartDate']
            SAR.PTExpiryDate = request.POST['PTExpiryDate']
            SAR.total = request.POST['total']
            SAR.Paid = request.POST['amtPaid']
            SAR.Remaining = request.POST['amtRemaining']
            SAR.Expiry = request.POST['serviceExpiryDate']

            SAR.save()
            AllSarthiServices = request.POST.getlist('myservice')
            SarthiServiesTracker.objects.filter(SarthiId = id).delete()
            for service in AllSarthiServices:
                SST = SarthiServiesTracker()
                SST.SarthiId = SAR.id
                SST.ServiceName = service
                SST.save()
            return redirect('RTOModSarthi')
    else:
        SARClasses = SarthiClasses.objects.all()
        SARServices = SarthiServices.objects.all()
        RawSSTs = SarthiServiesTracker.objects.filter(SarthiId=id).values_list('ServiceName', flat=True)
        SSTs = list(RawSSTs)
        return render(request,'RTOMod/sarthiEdit.html',{'SAR':SAR,'SARClasses':SARClasses,'SARServices':SARServices,'SSTs':SSTs})

def sarthiView(request,id):
    SAR = Sarthi.objects.get(pk=id)
    SARClasses = SarthiClasses.objects.all()
    SARServices = SarthiServices.objects.all()
    RawSSTs = SarthiServiesTracker.objects.filter(SarthiId=id).values_list('ServiceName', flat=True)
    SSTs = list(RawSSTs)
    return render(request,'RTOMod/SarthiView.html',{'SAR':SAR,'SARClasses':SARClasses,'SARServices':SARServices,'SSTs':SSTs})

def sarthiDelete(request,id):
    SAR = Sarthi.objects.get(pk=id)
    if request.method == 'POST':
        if 'SarthiDelete' in request.POST:
            SAR.delete()
            return redirect('RTOModSarthi')
    else:
        SARClasses = SarthiClasses.objects.all()
        SARServices = SarthiServices.objects.all()
        RawSSTs = SarthiServiesTracker.objects.filter(SarthiId=id).values_list('ServiceName', flat=True)
        SSTs = list(RawSSTs)
        return render(request,'RTOMod/SarthiDelete.html',{'SAR':SAR,'SARClasses':SARClasses,'SARServices':SARServices,'SSTs':SSTs})

def reports(request):
    
    return render(request, 'RTOMod/reports.html')

def reportsCash(request):
    if request.method =='POST':
        if 'cashReport' in request.POST:
            startDateStr = request.POST['FromDate']
            
            endDateStr = request.POST['ToDate']
            VahaanData = Sarthi.objects.filter(Q(created_at__gte=startDateStr) & Q(created_at__lte=endDateStr))
            SarthiData = Vahaan.objects.filter(Q(created_at__gte=startDateStr) & Q(created_at__lte=endDateStr))
            
            return render(request,'RTOMod/reportsCash.html',{'SarthiData':VahaanData,'VahaanData':SarthiData})
    else:
        return render(request,'RTOMod/reportsCash.html')

def reportsDaily(request):
    # if request.method =='POST':
    # startDateStr = request.POST['FromDate']
           
    VahaanData = Vahaan.objects.filter(created_at__date=datetime.now().date())
    SarthiData = Sarthi.objects.filter(created_at__date=datetime.now().date())
      
    print(VahaanData)
            
    return render(request,'RTOMod/reportsDaily.html',{'SarthiData':SarthiData,'VahaanData':VahaanData})
    # return render(request,'RTOMod/reportsDaily.html')
    
def settings(request):
    return render(request, 'RTOMod/settings.html')

def Tomorrow(request):
    return render(request, 'notification/Tomorrow.html')

def Today(request):
    data = Sarthi.objects.filter(Expiry=datetime.now().date())

    return render(request, 'notification/Today.html',{"SarthiData":data})

def SentSMSvahan(request):
    data = Sarthi.objects.filter(Expiry=datetime.now().date())
    numbers=[]
   
   


def importsarthi(request):
   
    # if  request.user.is_authenticated:
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sarthi.csv"'

    writer = csv.writer(response)
    writer.writerow([
               'Name',
               'contact',
               'DOB',
               'Class',
               'Address',
               'ApplicationNo',
               'EnrollmentNo',
               'LearningNo',
               'LicenseNo',
               'total',
               'Paid',
               'Remaining',
               'systemDate',
               'created_at',
               'updated_at',
        ])

    users = Vahaan.objects.all().values_list(
            'Name',
               'contact',
               'DOB',
               'Class',
               'Address',
               'ApplicationNo',
               'EnrollmentNo',
               'LearningNo',
               'LicenseNo',
               'total',
               'Paid',
               'Remaining',
               'systemDate',
               'created_at',
               'updated_at',
        )

    for user in users:
        writer.writerow(user)

    return response
    

def importvahaan(request):
   
    # if  request.user.is_authenticated:
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Vahan.csv"'

    writer = csv.writer(response)
    writer.writerow([
            'Name',
            'contact',
            'Address',
            'vehicleNo',
            'ClassId',
            'InsuranceNo',
            'InsuranceStartDate',
            'InsuranceExpiryDate',
            'PUCNo',
            'PUCStartDate',
            'PUCExpiryDate',
            'FitnessNo',
            'FitnessStartDate',
            'FitnessExpiryDate',
            'PermitNo',
            'PermitStartDate',
            'PermitExpiryDate',
            'TaxNo',
            'TaxStartDate',
            'TaxExpiryDate',
            'GTNo',
            'GTStartDate',
            'GTExpiryDate',
            'PTNo',
            'PTStartDate',
            'PTExpiryDate',
            'total',
            'Paid',
            'Remaining',
            'systemDate',
            'created_at',
            'updated_at',
                    ])

    users = Sarthi.objects.all().values_list(
            'Name',
            'contact',
            'Address',
            'vehicleNo',
            'ClassId',
            'InsuranceNo',
            'InsuranceStartDate',
            'InsuranceExpiryDate',
            'PUCNo',
            'PUCStartDate',
            'PUCExpiryDate',
            'FitnessNo',
            'FitnessStartDate',
            'FitnessExpiryDate',
            'PermitNo',
            'PermitStartDate',
            'PermitExpiryDate',
            'TaxNo',
            'TaxStartDate',
            'TaxExpiryDate',
            'GTNo',
            'GTStartDate',
            'GTExpiryDate',
            'PTNo',
            'PTStartDate',
            'PTExpiryDate',
            'total',
            'Paid',
            'Remaining',
            'systemDate',
            'created_at',
            'updated_at',
        )

    for user in users:
        writer.writerow(user)

    return response


def vahanprint(request,id):
    response = HttpResponse(content_type='text/pdf')
    response['Content-Disposition'] = 'attachment; filename="Vahaan.pdf"'
    data= Sarthi.objects.get(id=id)
    response['Content-Transfer-Encoding'] = 'binary'
    html_string =render_to_string('pdf/vahanpdf.html',{'data':data,'date':datetime.now().date()})
    html = HTML(string=html_string)
    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        
        output.seek(0)
        response.write(output.read())
       
    return response
    
    

def sarthiprint(request,id):
    response = HttpResponse(content_type='text/pdf')
    response['Content-Disposition'] = 'attachment; filename="sarthi.pdf"'
    data= Vahaan.objects.get(id=id)
    response['Content-Transfer-Encoding'] = 'binary'
    html_string =render_to_string('pdf/sarthipdf.html',{'data':data,'date':datetime.now().date()})
    html = HTML(string=html_string)
    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        
        output.seek(0)
        response.write(output.read())
       
    return response
    
    
def importonlysarthi(request):
  
    pass
    
def importonlyvahaan(request):
    """
    docstring
    """
    pass


