"""LeadGeneation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from LeadGenerationApp import views
from LeadGenerationApp import managerview
from LeadGenerationApp import customerview
from LeadGenerationApp import login
from LeadGenerationApp import callview

urlpatterns = [
    
    path('admin/', admin.site.urls),
    url(r'^api/employeeinterface', views.EmployeeInterface), 
    url(r'^api/employeesubmit', views.EmployeeSubmit),
    url(r'^api/employeelist', views.Employee_List),
    url(r'^api/displayallemployee', views.DisplayAllEmployee),
    url(r'^api/employeebyid',views.Employee_List_By_Id),   
    url(r'^api/employeeupdatedelete',views.Employee_Update_Delete), 
    url(r'^api/display_employee_picture',views.Employee_Display_Picture),   
    url(r'^api/update_employee_image',views.UpdateEmployeeImage), 
    
    url(r'^api/statelist', views.State_List),
    url(r'^api/citylist', views.City_List),

    url(r'^api/managerinterface',managerview.ManagerInterface), 
    url(r'^api/managersubmit',managerview.ManagerSubmit), 
    url(r'^api/managerlist',managerview.Manager_List), 
    url(r'^api/displayallmanager',managerview.DisplayAllManager), 
    url(r'^api/managerbyid',managerview.Manager_List_By_Id),   
    url(r'^api/managerupdatedelete',managerview.Manager_Update_Delete), 
    url(r'^api/display_manager_picture',managerview.Manager_Display_Picture),   
    url(r'^api/update_manager_image',managerview.UpdateManagerImage),   
    

    url(r'^api/customerinterface', customerview.CustomerInterface), 
    url(r'^api/customersubmit', customerview.CustomerSubmit),
    url(r'^api/customerlist', customerview.Customer_List),
    url(r'^api/displayallcustomer', customerview.DisplayAllCustomer),
    url(r'^api/customerbyid',customerview.Customer_List_By_Id),   
    url(r'^api/customerupdatedelete',customerview.Customer_Update_Delete), 
    url(r'^api/display_customer_picture',customerview.Customer_Display_Picture),   
    url(r'^api/update_customer_image',customerview.UpdateCustomerImage), 

    url(r'^api/login',login.LoginInterface), 
    
    url(r'^api/admindashboard',login.AdminDashboard),
    url(r'^api/checkadminlogin',login.Check_Admin_Login),
    url(r'^api/logoutadmin',login.LogoutAdmin), 
    url(r'^api/update_adminprofile_pic',login.UpdateAdminProfilePic),
    url(r'^api/adminupdate',login.UpdateAdmin), 
    
    url(r'^api/managerdashboard',login.ManagerDashboard),
    url(r'^api/checkmanagerlogin',login.Check_Manager_Login),
    url(r'^api/update_managerprofile_pic',login.UpdateManagerProfilePic),   
    url(r'^api/managerupdate',login.UpdateManager), 
    url(r'^api/logoutmanager',login.LogoutManager), 
       
       
    url(r'^api/employeedashboard',login.EmployeeDashboard),
    url(r'^api/checkemployeelogin',login.Check_Employee_Login),
    url(r'^api/logoutemployee',login.LogoutEmployee), 
    url(r'^api/update_employeeprofile_pic',login.UpdateEmployeeProfilePic),
    url(r'^api/employeeupdate',login.UpdateEmployee), 
       
        
    url(r'^api/homepage',login.HomePage), 
    url(r'^api/calldetails/',login.CallDetails), 
    
    

    url(r'^api/callcustomerbyid',callview.Customer_List_By_Id),
    url(r'^api/calldetailsubmit',callview.CallDetailSubmit),
    url(r'^api/displayallcalldetails', callview.DisplayAllCallDetails),
    url(r'^api/calldetailslist', callview.CallDetails_List),
    

]
