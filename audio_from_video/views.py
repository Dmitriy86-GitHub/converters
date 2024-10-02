from django.shortcuts import render
from django.views import View
from . forms import VideoUploadForm
from django.http import HttpResponseRedirect
# Create your views here.
def home_page(request):
    return render(request, 'audio_from_video/homepage.html')

# def audio_from_video(request):
#     return render(request, 'audio_from_video/audio_from_video.html' )

def storag_file(file):
    with open('video_files/{file.name}','wb+') as new_file:
        for chunk in file.chunks():
            new_file.write(chunk)

class VideoView(View):
    def get(self,request):
        form = VideoUploadForm()
        return render(request,'audio_from_video/audio_from_video.html', {'form':form})
    def post(self,request):
        form = VideoUploadForm(request.POST,request.FILES)
        if form.is_valid():
            storag_file(form.cleaned_data['video'])
            # return HttpResponseRedirect('/')
        return render(request, 'audio_from_video/audio_from_video.html',{'form':form})