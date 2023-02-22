from django.shortcuts import render
from rest_framework.decorators import api_view
from django.db import connection
from .import tuple_to_dict
from django.http.response import JsonResponse
from django.shortcuts import redirect
from LeadGenerationApp.models import Administrator
from LeadGenerationApp.models import Manager

# For showing pade in dashboard 
from django.views.decorators.clickjacking import xframe_options_exempt

from django.shortcuts import render


# ----------------Login----------------------------------------

@api_view(['GET', 'POST', 'DELETE'])
def LoginInterface(request):
    return render(request,"login.html",{})

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def HomePage(request):
    return render(request,"Home.html",{})


@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def CallDetails(request):
    cursor=connection.cursor() 
    q="select c.*, (select count(*) from leadgeneration.leadgenerationapp_calldetail where  leadstatus=Hot) as h ,(select count(*) from leadgeneration.leadgenerationapp_calldetail where  leadstatus=warm ) as w,(select count(*) from leadgeneration.leadgenerationapp_calldetail where  leadstatus=cold ) as co,(select count(*) from leadgeneration.leadgenerationapp_calldetail  where  leadstatus=freeze ) as fre,(select count(*) from leadgeneration.leadgenerationapp_calldetail  where  phonestatus=connected ) as conn,(select count(*) from leadgeneration.leadgenerationapp_calldetail where  phonestatus=disconnected ) as diss from leadgeneration.leadgenerationapp_calldetail c;"

    # print("---------------------------",q)
    cursor.execute(q)
    data=cursor.fetchall()    
    # print(data)
    return render(request,"Home.html",{'record':data})






# --------------ADMIN-----------------------------------------

def AdminDashboard(request):
    try: 
     admin=request.session['ADMIN']
     print("Admin Session:",admin)
     return render(request,"AdminDashboard.html",{'admin':admin})
    except:
     return render(request,"Login.html",{}) 


@api_view(['GET', 'POST', 'DELETE'])
def Check_Admin_Login(request):
   if request.method=='GET':
    cursor=connection.cursor() 
    q="select * from leadgenerationapp_administrator where mobileno='{0}' and password='{1}'".format(request.GET['mobileno'],request.GET['password'])
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictAll(cursor)
    if(len(data)==1):
      #  Session logic
     print("ADMIN DATA:",data)   
     request.session['ADMIN']=data
     return JsonResponse({"data":data,"status":True},safe=False)
    else:
     return JsonResponse({"data":{},"status":False},safe=False)   
   return JsonResponse({},safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def LogoutAdmin(request):
    del request.session['ADMIN']
    return render(request,"Login.html",{})


@api_view(['GET', 'POST', 'DELETE'])
def UpdateAdminProfilePic(request):
  if request.method == 'POST':
     admin=Administrator.objects.get(pk=request.POST['id']) 
     admin.Profilepic=request.FILES['Profilepic']
     admin.save()
  return redirect('/api/admindashboard')   


@api_view(['GET', 'POST', 'DELETE'])
def UpdateAdmin(request):
   if request.method=='GET':
      btn=request.GET['btn']
      if(btn=='Edit'):
       admin=Administrator.objects.get(pk=request.GET['id']) 
       admin.adminname=request.GET['newadminname']
       admin.emailid=request.GET['newemailid']
       admin.mobileno=request.GET['newmobileno']
       admin.password=request.GET['newpassword']
       admin.save()
      else:
        admin=Administrator.objects.get(pk=request.GET['id']) 
        admin.delete()  
   return redirect('/api/admindashboard')



# ---------------Manager--------------------------------------
def ManagerDashboard(request):
    try: 
     manager=request.session['MANAGER']
     print("Manager Session:",manager)
     return render(request,"ManagerDashboard.html",{'manager':manager})
    except:
     return render(request,"Login.html",{}) 

@api_view(['GET', 'POST', 'DELETE'])
def Check_Manager_Login(request):
   if request.method=='GET':
    cursor=connection.cursor() 
    q="select * from leadgenerationapp_manager where mobileno='{0}' and password='{1}'".format(request.GET['mobileno'],request.GET['password'])
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictAll(cursor)
    if(len(data)==1):
      #  Session logic
     print("Manager DATA:",data)   
     request.session['MANAGER']=data
     return JsonResponse({"data":data,"status":True},safe=False)
    else:
     return JsonResponse({"data":{},"status":False},safe=False)   
   return JsonResponse({},safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def UpdateManagerProfilePic(request):
  if request.method == 'POST':
     manager=Manager.objects.get(pk=request.POST['id']) 
     manager.Profilepic=request.FILES['Profilepic']
     print("-------------",manager.Profilepic)
     manager.save()
  return redirect('/api/managerdashboard')


@api_view(['GET', 'POST', 'DELETE'])
def UpdateManager(request):
   if request.method=='GET':
      btn=request.GET['btn']
      if(btn=='Edit'):
       manager=Manager.objects.get(pk=request.GET['id']) 
       manager.firstname=request.GET['newfirstname']
       manager.lastname=request.GET['newlastname']
       manager.emailid=request.GET['newemailid']
       manager.mobileno=request.GET['newmobileno']
       manager.password=request.GET['newpassword']
       manager.save()
      else:
        manager=Administrator.objects.get(pk=request.GET['id']) 
        manager.delete()  
   return redirect('/api/managerdashboard')



@api_view(['GET', 'POST', 'DELETE'])
def LogoutManager(request):
    del request.session['MANAGER']
    return render(request,"Login.html",{})


# -------------Employee---------------------------------------
def EmployeeDashboard(request):
    try: 
     employee=request.session['EMPLOYEE']
     print("Employee Session:",employee)
     return render(request,"EmployeeDashboard.html",{'employee':employee})
    except:
     return render(request,"Login.html",{})         



@api_view(['GET', 'POST', 'DELETE'])
def Check_Employee_Login(request):
   if request.method=='GET':
    cursor=connection.cursor() 
    q="select * from leadgenerationapp_employee where mobileno='{0}' and password='{1}'".format(request.GET['mobileno'],request.GET['password'])
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictAll(cursor)
    if(len(data)==1):
      print("Employee DATA:",data)   
      request.session['EMPLOYEE']=data
      return JsonResponse({"data":data,"status":True},safe=False)
    else:
     return JsonResponse({"data":{},"status":False},safe=False)   
   return JsonResponse({},safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def LogoutEmployee(request):
    del request.session['EMPLOYEE']
    return render(request,"Login.html",{})


@api_view(['GET', 'POST', 'DELETE'])
def UpdateEmployeeProfilePic(request):
  if request.method == 'POST':
     admin=Administrator.objects.get(pk=request.POST['id']) 
     admin.Profilepic=request.FILES['Profilepic']
     admin.save()
  return redirect('/api/admindashboard')   


@api_view(['GET', 'POST', 'DELETE'])
def UpdateEmployee(request):
   if request.method=='GET':
      btn=request.GET['btn']
      if(btn=='Edit'):
       admin=Administrator.objects.get(pk=request.GET['id']) 
       admin.adminname=request.GET['newadminname']
       admin.emailid=request.GET['newemailid']
       admin.mobileno=request.GET['newmobileno']
       admin.password=request.GET['newpassword']
       admin.save()
      else:
        admin=Administrator.objects.get(pk=request.GET['id']) 
        admin.delete()  
   return redirect('/api/admindashboard')

