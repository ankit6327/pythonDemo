from django.shortcuts import render

# Create your views here.

def music_list(request):
    return render(request, 'music/music_list.html', {})