from django.shortcuts import render,redirect
from pytube import YouTube
from django.http import HttpResponse

def home(request):
	return render(request,'home.html')


def pre_down(request):
	if request.method=='POST':
		try:
			link=request.POST['link']
			video=YouTube(link)
			img=video.thumbnail_url
			download=video.streams[0].url
			return render(request,'pre_down.html',{'link':link,'img':img,'download':download})
		except:
			return HttpResponse('404 Not found')
	return redirect('home')

