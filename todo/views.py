from .serializers import TodoSerializer 
from .models import Todo 
from rest_framework.decorators import api_view
from rest_framework.response import Response 


@api_view(['GET'])
def ApiUrl(request):
    todo_urls = {
            'List' : '/todo-list',
            'Detail View' : '/todo-body/<str:pk>/',
            'Create' : '/todo-create/',
            'Update' : '/todo-update/<str:pk>/',
            'Delete' : '/todo-delete/<str:pk>/'
            } 
    return Response(todo_urls)


### Get List of TODOS
@api_view(['GET'])
def TodoList(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

### Get Single Todo
@api_view(['GET'])
def TodoBody(request, pk):
    todos = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todos, many=False)
    return Response(serializer.data)

### Update Todo
@api_view(['POST'])
def TodoUpdate(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=todo, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

### Create new Todo
@api_view(['POST'])
def TodoCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

### Delete Todo
@api_view(['DELETE'])
def TodoDelete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return Response("Sucessfully deleted")
