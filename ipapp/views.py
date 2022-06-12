from cProfile import label
from genericpath import exists
from ipaddress import ip_address
import django
from django.shortcuts import render,HttpResponseRedirect,redirect
import requests
from urllib3 import Retry
from.models import Searched_data,Chart_table
from .forms import ip_form
from django.contrib.auth.decorators import login_required # used to restrict acessing pages
from .forms import NewUserForm
from django.contrib.auth import login, authenticate,logout      # for login 
from django.contrib.auth.forms import AuthenticationForm #for auth login
from django.contrib.auth import login
from django.contrib import messages
from django.db.models import Count
import folium
from folium import plugins
import geocoder
import json


def homepage(request):

    return render(request, 'ipapp/homepage.html')

#user registration
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("ipapp:login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="ipapp/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("ipapp:index2")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="ipapp/login.html", context={"login_form":form} )




@login_required(login_url='ipapp:login')
def index2(request):
   form = ip_form()
   if request.method == 'POST':
        form = ip_form( request.POST)
        s = form.data.get('ip')
        #print(str(s))
        response = requests.get('http://ipwho.is/'+s)
        my_info = response.json()
        print(my_info)
        current_user = request.user # getting the current user
        print(current_user)
        dat={       
                   'ip'          : my_info['ip'],
                   'continent'   : my_info['continent'],
                    'country'    : my_info['country'],
                    'country_code': my_info['country_code'],
                    'region'      : my_info['region'],
                    'region_code' : my_info['region_code'],
                    'city'        : my_info['city'],
                    'lat'         :my_info['latitude'],
                    'lng'         :my_info['longitude'],
                    'user'        :current_user,
              }
        check =dat.get('continent')
        print(check)

        objectmain =Searched_data(** dat)
        objectmain.save()
        #for key, value in dat:
        #    if key == form.fields.keys :
        #        form.as_table()
#
        #    if form.is_valid():
        #       
        #       form.save()
   
   data_base = Searched_data.objects.all()
     
   

   return render (request,'ipapp/index2.html',{'form':form})


@login_required(login_url='ipapp:login')
def chart(request):
    Chart_table.objects.all().delete() #enables overwriting of the chart table
    chart_items = Searched_data.objects.all().values('country','user','lat','lng').annotate(total=Count('country')) # This checks the number of occurence in the searched api by country
    
    #this gets the country ,total and user
    for item in chart_items:
        
             Chart_table.objects.create(label=item['country'], data=item['total'],user=item['user'],lat=item['lat'],lng=item['lng'])
      
    map1 = folium.Map(tiles ='cartoDB Dark_Matter', location=[40, -99], zoom_start=2)
    
    data_plug = [[19,-12,300],[20,10,9000]] # long,lat,magnitude(that is what yo are mesuring)
    data_list = Chart_table.objects.values_list('lat','lng','data')
    print(data_list)

    plugins.HeatMap(data_list).add_to(map1)
    map1 =map1._repr_html_()
   
   #Graph for pie and line graph

    labels =[]
    data_set =[]
    query_set = Chart_table.objects.order_by('-data')
    for query in  query_set:
       labels.append(query.label)
       data_set.append(query.data)
       print(labels)

    my_context1 = {

         'map1'     : map1,
         'labels'   : labels,
         'data_set' : data_set

    }
       
       
    return render(request, 'ipapp/chart.html',my_context1)








@login_required(login_url='ipapp:login')
def table (request):
    # this gets the required information/fields from the data base.
   data_base = Searched_data.objects.all().values('ip','continent','country','country_code','region','region_code','city','user')
   
   test_all = json.dumps({"data": list(data_base)})
    
   print(test_all)
   my_context = { 
       'test_all': test_all,
       }
    
   return render(request,'ipapp/table.html',my_context)




     




def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("ipapp:login")
































    
    
    
    
   



    
     

      








