from django.shortcuts import render, redirect

from .models import Todo_List
from .forms import Todo_Item_Form

# Create your views here.
def Todo(request):
    if request.method == 'POST':
        form = Todo_Item_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Todo')
        else:
            form = Todo_Item_Form()

    todo_items = Todo_List.objects.all()
    context = {'todo_items': todo_items}
    return render(request, 'index.html', context)


def completed(request):
    completed_items = Todo_List.objects.filter(completed=True)
    context = {'completed_items': completed_items}
    return render(request, 'completed.html', context)

def not_completed(request):
    not_completed_items = Todo_List.objects.filter(completed=False)
    context = {'not_completed_items': not_completed_items}
    return render(request, 'not_completed.html', context)

def completed_todo_item(request, todo_item_id):
    todo_item = Todo_List.objects.get(pk=todo_item_id)
    todo_item.completed = not todo_item.completed
    todo_item.save()
    return redirect('Todo')