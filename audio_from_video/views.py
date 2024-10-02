from django.shortcuts import render
from django.views import View
from . forms import VideoUploadForm
import moviepy.editor




# Create your views here.
def home_page(request):
    return render(request, 'audio_from_video/homepage.html')


def storag_file(file):
    with open('audio_from_video/video_files/my_file','wb+') as new_file:
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
            video = moviepy.editor.VideoFileClip('audio_from_video/video_files/my_file')
            audio = video.audio
            audio.write_audiofile('audio_from_video/audio_files/my_audio.mp3')
            # return HttpResponseRedirect('/')
        return render(request, 'audio_from_video/audio_from_video.html',{'form':form})

