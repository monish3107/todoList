from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from home.models import Task

# login: admin, admin

# Create your views here.
def home(request):
    context = {'success': False}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success': True}
    return render(request, 'index.html', context)

def task(request):
    search_query = request.GET.get('search', '')  
    if search_query:
        allTasks = Task.objects.filter(taskTitle__icontains=search_query) 
    else:
        allTasks = Task.objects.all() 

    context = {'tasks': allTasks}
    return render(request, 'task.html', context)

def toggle_task_completion(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed  
    task.save()
    return redirect('tasks')
