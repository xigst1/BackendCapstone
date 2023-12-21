from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import permissions

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data)
        
        
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        
        else:
            return Response({'status': 'failed'})
        
        
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        menuItem = get_object_or_404(Menu, pk=pk)
        serializer = MenuSerializer(menuItem, many=False)
        return Response(serializer.data)
 
    
    def put(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        menuItem = get_object_or_404(Menu, pk=pk)
        
        if menuItem.Title != request.data['Title']:
            menuItem.Title = request.data['Title']
        if menuItem.Price != request.data['Price']:
            menuItem.Price = request.data['Price']
        if menuItem.Inventory != request.data['Inventory']:
            menuItem.Inventory = request.data['Inventory']
        
        menuItem.save()
        return Response({'status': 'success', 'data': MenuSerializer(menuItem).data})  

    
    def delete(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        menuItem = get_object_or_404(Menu, pk=pk)
        menuItem.delete()
        # serializer = MenuSerializer(menuItem, many=False)
        
        return Response({'status': 'success'})

        
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    


