from django.shortcuts import render
from rest_framework import viewsets,generics, permissions
from rest_framework.decorators import permission_classes,api_view
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer,MenuSerializer,BookingSerializer
from .models import Menu,Booking

# Create your views here.
def index(request):
    return render(request, 'index.html')

@permission_classes([IsAuthenticated])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@permission_classes([IsAuthenticated])    
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

@permission_classes([IsAuthenticated])    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    #permission_classes = [permissions.IsAuthenticated]
    
@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message":"This view is protected."})
