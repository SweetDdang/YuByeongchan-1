from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.http import HttpResponse
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



def main(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    
    ctx = {
        'posts': posts,
        'comments' : comments,
    }
    return render(request, 'main.html', ctx)


@csrf_exempt
def like(request):
    req =json.loads(request.body)
    id = req['id']
    type = req['type']
    post = Post.objects.get(id = id)

    if type == 'like':
        post.like += 1
    else:
        pass
    
    post.save()
    return JsonResponse({'id': id, 'type': type})


@csrf_exempt
def add_comment(request):
    req = json.loads(request.body)
    id = req['id']
    type = req['type']
    content = req['content']
    comment = Comment()
    comment.post = Post.objects.get(id = id)
    comment.content = content
    comment_id = comment.id
    comment.save()
    return JsonResponse({'id': id, 'type': type, 'content': content, 'comment-id': comment_id})

@csrf_exempt
def del_comment(request):
    req = json.loads(request.body)
    comment_id = req['id']
    comment = get_object_or_404(Comment, id = comment_id)
    comment.delete()
    return JsonResponse({'id': comment_id})