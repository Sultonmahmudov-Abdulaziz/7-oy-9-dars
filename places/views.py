from django.shortcuts import render
from .models import Place
from django.views import View



class PlaceListView(View):
    def get(self, request):

        places = Place.objects.all()
        return render(request, template_name= 'places/list.html', context={'places': places})
class PlaceDetailView(View):

    def get(self, request,pk):

        place = Place.objects.get(pk=pk)
        return render(request, template_name= 'places/detail.html', context={'place': place})