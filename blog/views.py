from django.shortcuts import render , get_object_or_404
from .models import Postblog

def post_list_view(request):
    #posts_list = Postblog.objects.all()
    posts_list = Postblog.objects.filter(status = 'pub')
    return render (request,'blog/post_list.html', {'posts_list': posts_list})

def post_detail_view(request, pk):
    post = get_object_or_404(Postblog,pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
    