from .models import Message
from .serializers import MessagesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class MessageList(APIView):

    def get(self, request):
        messages = Message.objects.all()
        serializer = MessagesSerializer(messages,many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = MessagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
