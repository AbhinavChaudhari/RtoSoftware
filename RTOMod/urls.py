from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name="RTOModIndex"),
    path('vahaan/', views.vahaan, name="RTOModVahaan"),
    path('vahaan/register/', views.vahaanRegister, name="RTOModVahaanRegister"),
    path('vahaan/edit/<id>', views.vahaanEdit, name="RTOModVahaanEdit"),
    path('vahaan/view/<id>', views.vahaanView, name="RTOModVahaanView"),
    path('vahaan/delete/<id>', views.vahaanDelete, name="RTOModVahaanDelete"),
    path('sarthi/', views.sarthi, name="RTOModSarthi"),
    path('sarthi/register/', views.sarthiRegister, name="RTOModSarthiRegister"),
    path('Sarthi/edit/<id>', views.sarthiEdit, name="RTOModSarthiEdit"),
    path('Sarthi/view/<id>', views.sarthiView, name="RTOModSarthiView"),
    path('Sarthi/delete/<id>', views.sarthiDelete, name="RTOModSarthiDelete"),
    
    path('reports/', views.reports, name="RTOModReports"),
    path('settings/', views.settings, name="RTOModSettings"),

    # notification
    path("Today/", views.Today, name="Today"),
    path("Tomorrow/", views.Tomorrow, name="Tomorrow"),
    path("SentSMSvahan/", views.SentSMSvahan, name="SentSMSvahan"),


    # export 
    path("importsarthi/", views.importsarthi, name="importsarthi"),
    path("importvahaan/", views.importvahaan, name="importvahaan"),

    # import 
    path("admin/RTOMod/vahaan/", views.importonlysarthi,name="importonlysarthi"),
    path("admin/RTOMod/sarthi/", views.importonlyvahaan,name="importonlyvahaan"),

    # report
    path('reports/', views.reports, name="RTOModReports"),
    path('reports/cash/', views.reportsCash, name="RTOModReportsCash"), 
    path('reports/daily/', views.reportsDaily, name="RTOModReportsDaily"),


    # pdfprint
    path('vahanprint/<id>', views.vahanprint, name="vahanprint"),
    path('sarthiprint/<id>', views.sarthiprint, name="sarthiprint"),

  

]
