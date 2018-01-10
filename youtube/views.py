from django.shortcuts import render
from django.http import HttpResponse
import pafy

# Create your views here.
def index(request):
	return render(request, "youtube/index.html", {})

def video(request):
	video = pafy.new(request.GET['url'])
	best = video.getbestvideo(preftype='mp4')
	return render(request, 'youtube/video.html', {'url':best.url,'title_video': video.title,'descripcion':video.description, 'id_video':video.videoid, 'video_author':video.author, 'video_likes':video.likes, 'video_dislikes':video.dislikes, 'filename':best.filename})
