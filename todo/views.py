from django.shortcuts import render,redirect
from.models import Todo
from.forms import TodoForm,NewTodoForm
from django.views.decorators.http import require_POST

# Create your views here.
def Index(request):
    todo_list=Todo.objects.order_by('id')
    #form=TodoForm()
    newtodoform=NewTodoForm()
    context={'todo_list':todo_list,'form':newtodoform}
    return render(request,'todo/index.html',context)

@require_POST
def addtodo(request):
    form=TodoForm(request.POST)
    print(request.POST['text'])
    if form.is_valid():
        new_todo=Todo(text=form.cleaned_data['text'])
        new_todo.save()

    return redirect('index')

def completetodo(request,todo_id):
    todo=Todo.objects.get(pk=todo_id)
    todo.complete=True
    todo.save()
    return redirect('index')

def deletecomplete(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')

def deleteall(request):
    Todo.objects.all().delete()
    return redirect('index')