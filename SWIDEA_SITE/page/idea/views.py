from django.shortcuts import render, redirect, get_object_or_404
from .models import Idea, Dev_tool
from .forms import IdeaForm, DevForm


def idea_list(request):
    ideas = Idea.objects.all()
    ctx = {'ideas': ideas}

    return render(request, template_name = 'idea/idea_list.html', context = ctx )

def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save()
            return redirect('idea:idea_list')
    else :
        form = IdeaForm()
        ctx = {'form' : form}
        return render(request, template_name = 'idea/idea_form.html', context = ctx )

def idea_detail(request, pk):
    idea = Idea.objects.get(id=pk)
    ctx = {'idea': idea}

    return render(request, template_name = 'idea/idea_detail.html', context = ctx )


def idea_update(request, pk):
    idea = get_object_or_404(Idea, id=pk)
    
    if request.method == 'POST' :
        form = IdeaForm(request.POST, instance = idea)
        if form.is_valid():
            idea = form.save()
            return redirect('idea:idea_detail',pk)
    else : 
        form = IdeaForm(instance = idea)
        ctx = {'form' : form}
        return render(request, template_name = 'idea/idea_form.html', context = ctx )

def idea_delete(request, pk):
    idea = get_object_or_404(Idea, id=pk)
    idea.delete()
    return redirect('idea:idea_list')



def dev_list(request):
    dev = Dev_tool.objects.all()
    ctx = {'devs': dev}

    return render(request, template_name='idea/dev_list.html', context=ctx)


def dev_create(request):
    if request.method == 'POST':
        form = DevForm(request.POST)
        if form.is_valid():
            dev = form.save()

            return redirect('idea:dev_list', pk=dev.pk)
    else:
        form = DevForm()
        ctx = {'form': form}
        
        return render(request, template_name='idea/dev_form.html', context=ctx)

def dev_detail(request, pk):
    dev = get_object_or_404(Dev_tool, pk=pk)
    idea = Idea.objects.filter(Dev_tool=dev)
    ctx = {'devs': dev, 'ideas':idea}

    return render(request, template_name='idea/dev_detail.html', context=ctx)

def dev_update(request, pk):
    dev = get_object_or_404(Dev_tool, pk=pk)
    if request.method == 'POST':
        form = DevForm(request.POST, instance=dev)
        if form.is_valid():
            dev = form.save()
            return redirect('idea:dev_detail', pk)
    else:
        form = DevForm(instance=dev)
        ctx = {'form': form}
        return render(request, template_name='idea/dev_form.html', context=ctx)

def dev_delete(request, pk):
    dev = get_object_or_404(Dev_tool, pk=pk)
    dev.delete()

    return redirect('ideas:dev_list')