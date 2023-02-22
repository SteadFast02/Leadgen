from django.shortcuts import render
from rest_framework.decorators import api_view

from LeadGenerationApp.serializers import CustomerSerializer
from LeadGenerationApp.models import Customer
from django.http.response import JsonResponse
from django.db import connection
from .import tuple_to_dict
from django.shortcuts import redirect

# For showing pade in dashboard 
from django.views.decorators.clickjacking import xframe_options_exempt


# For showing pade in dashboard     
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def CustomerInterface(request):
    return render(request,"Customer.html",{})

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def CustomerSubmit(request):
  
  if request.method == 'POST':
 
    #employee_data = request.GET.dict()
    print("Customer",request.data)
    customer_serializer = CustomerSerializer(data=request.data)
    if customer_serializer.is_valid():
        customer_serializer.save()
        return render(request,"Customer.html",{"message":"Record Submitted Successfully"})

  return render(request,"Customer.html",{"message":"Server Error:Fail to Submit Record"})

# For showing pade in dashboard     
@xframe_options_exempt
def DisplayAllCustomer(request):
    return render(request,"DisplayAllCustomer.html",{})

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Customer_List(request):
   if request.method=='GET':
    cursor=connection.cursor() 
    q="select C.*,(select S.statename from leadgenerationapp_states S where S.stateid=C.state) as statename,(select C.cityname from leadgenerationapp_cities C where C.cityid=C.city) as cityname from leadgenerationapp_customer C"
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictAll(cursor)
    return JsonResponse(data,safe=False)
  
   return JsonResponse({},safe=False)  

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Customer_List_By_Id(request):
   if request.method=='GET':
    customerid=request.GET['customerid']
    cursor=connection.cursor() 
    q="select C.*,(select S.statename from leadgenerationapp_states S where S.stateid=C.state) as statename,(select C.cityname from leadgenerationapp_cities C where C.cityid=C.city) as cityname from leadgenerationapp_customer C where C.id={0}".format(customerid)
   #  print("---------------------------",q)
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictOne(cursor)
   #  print("date",data['dob'])
    data['dob']=str(data['dob'])
    if(data['gender']=='Male'):mg=True 
    else:mg=False
    if(data['gender']=='Female'):fg=True 
    else:fg=False
    return render(request,"CustomerById.html",{'record':data,'mgender':mg,'fgender':fg})
  
   return JsonResponse({},safe=False) 

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Customer_Update_Delete(request):
   if request.method=='GET':
      btn=request.GET['btn']
      if(btn=='Edit'):
       customer=Customer.objects.get(pk=request.GET['id']) 
       customer.firstname=request.GET['firstname']
       customer.lastname=request.GET['lastname']
       customer.dob=request.GET['dob']
       customer.gender=request.GET['gender']
       customer.emailid=request.GET['emailid']
       customer.mobileno1=request.GET['mobileno1']
       customer.organization=request.GET['organization']
       customer.mobileno2=request.GET['mobileno2']
       customer.address=request.GET['address']
       customer.state=request.GET['state']
       customer.city=request.GET['city']
       customer.save()
      else:
        customer=Customer.objects.get(pk=request.GET['id']) 
        customer.delete()  
   return redirect('/api/displayallcustomer')

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Customer_Display_Picture(request):
   if request.method=='GET':
      return render(request,"CustomerPicture.html",{"id":request.GET['customerid'],"customername":request.GET['customername'],'picture':request.GET['picture']})

@xframe_options_exempt  
@api_view(['GET', 'POST', 'DELETE'])
def UpdateCustomerImage(request):
  
  if request.method == 'POST':
     customer=Customer.objects.get(pk=request.POST['id']) 
     customer.photograph=request.FILES['photograph']
     customer.save()
  return redirect('/api/displayallcustomer')    