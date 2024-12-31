from rest_framework import generics, permissions
from .serializers import TodoSerializer
from todo.models import Todo
from rest_framework.parsers import JSONParser
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User



class TodosListCreate(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-created_at') 
    

    def perform_create(self, serializer):
         return super().perform_create(serializer)


class TodosRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
        
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)
        


class TodoToggleComplete(generics.UpdateAPIView):
    serializer_class = TodoSerializer
    permission_class = [permissions.IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)
    
    def perform_update(self,serializer):
        serializer.instance.completed=not(serializer.instance.completed)
        serializer.save()




@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(username=data['username'], password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
        except IntegrityError:
            return JsonResponse({'error': 'username taken choose another username'}, status=400)
        



        