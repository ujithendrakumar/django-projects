import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import City
from .forms import CityForm
# Create your views here.
def home(request):
	url = "http://api.openweathermap.org/data/2.5/weather?q={},india&units=imperial&appid=d269c3ce77abdc3be249ee30c18bdac6"
	
	if request.method == 'POST':
		
		form = CityForm(request.POST)
		form.save()
		# print(request.POST)
	form = CityForm()

	cities = City.objects.all()
	city = 'Vijayawada'
	weather_data =[]
	for city in cities:
		r = requests.get(url.format(city)).json()
		# print(r)
		city_weather = {
					'city': city.name ,
					'temperature':r['main']['temp'] ,
					'description':r['weather'][0]['description'] ,
					'icon':r['weather'][0]['icon'] ,
			}
		weather_data.append(city_weather)
	# print(city_weather)
	 # print(weather_data)	
	context={'weather_data':weather_data,'form':form}
	
	return render(request,'weather/index.html',context)

 
def about(request):
	return HttpResponse('Hello Worlds Mr. Jithendra Kumar')
	