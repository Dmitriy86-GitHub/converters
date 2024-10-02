from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'audio_from_video/homepage.html')

def audio_from_video(request):
    return render(request, 'audio_from_video/audio_from_video.html' )