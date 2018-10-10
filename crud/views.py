from django.shortcuts import render, redirect
from .models import Player
from .forms import PlayerForm

# Create your views here.

def home(request):
	data = {}
	data['players'] = Player.objects.all()
	return render(request, 'index.html', data)

def new(request):
	form = PlayerForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('show')
	return render(request, 'new.html', {'playerForm':form})

def update(request, pk):
	player = Player.objects.get(pk=pk)
	form = PlayerForm(request.POST or None, instance=player)
	if form.is_valid():
		form.save()
		return redirect('show')
	return render(request, 'new.html', {'playerForm':form})

def delete(request, pk):
	player = Player.objects.get(pk=pk)
	player.delete();
	return redirect('show')
