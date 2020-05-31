
import requests
from django.http import Http404
from django.views.generic import DeleteView
from django.shortcuts import render, get_object_or_404, reverse
from .models import City
from django.urls import reverse_lazy
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=141f0fb7e29479363cd0ab487a6fe816'

    if request.method == 'POST':
        form = CityForm(request.POST)
        
        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()
            
            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                
                if r['cod'] == 200:
                    form.save()
                else:
                    raise Http404('That is not a valid City')
            else:
                raise Http404('The City Already exists')

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'pk': city.id,
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/weather.html', context)


class CityDeleteView(DeleteView):
    model = City
    # template_name = 'weather.html'
    success_url = reverse_lazy('weather:home')

    #This makes it so their isnt a confirmation page being loaded
    def get(self, request, *args, **kwargs):
        return self.post(request,*args, **kwargs)
   
    #Gets object that we want to pass to URLconf
    def get_object(self):
        return City.objects.get(name=self.kwargs.get('name'))


    