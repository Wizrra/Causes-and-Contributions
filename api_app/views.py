from rest_framework import generics
from .models import Contribute, Causes
from rest_framework.response import Response
from .serializers import ContributeSerializer, CausesSerializer
from rest_framework import status

class CauseListCreateView(generics.ListCreateAPIView):
  queryset = Causes.objects.all()
  serializer_class = CausesSerializer

  def get(self, request, *args, **kwargs):
    id = self.kwargs.get('id')
    if id:
      try:
        causes = self.get_queryset().get(id=id)
      except Causes.DoesNotExist:
        return Response({'message': 'Causes not found'}, status=status.HTTP_404_NOT_FOUND)
      serializer = self.get_serializer(causes, many=False)
    else:
      causes = self.get_queryset()
    serializer = self.get_serializer(causes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({
        'message': 'Cause created successfully', 
        'cause': serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response({
      'message': 'Failed to create cause',
      'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)
  

class CauseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Causes.objects.all()
    serializer_class = CausesSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Cause updated successfully',
                'cause': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Failed to update cause',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            'message': 'Cause deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)

# class ContributeCreateView(generics.CreateAPIView):
#     queryset = Contribute.objects.all()
#     serializer_class = ContributeSerializer
#     lookup_field = 'id'

#     def create(self, request, *args, **kwargs):
#         cause_id = self.kwargs.get('id')
#         try:
#             cause = Causes.objects.get(id=cause_id)
#         except Causes.DoesNotExist:
#             return Response({
#                 'message': 'Contrib not found'
#             }, status=status.HTTP_404_NOT_FOUND)

#         # Add cause to request data for serializer validation
#         data = request.data.copy()
#         data['causes'] = str(cause_id)
        
#         serializer = self.get_serializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'message': 'Contribution created successfully',
#                 'contribution': serializer.data
#             }, status=status.HTTP_201_CREATED)
#         return Response({
#             'message': 'Failed to create contribution',
#             'errors': serializer.errors
#         }, status=status.HTTP_400_BAD_REQUEST)
    
    
# Change CreateAPIView to ListCreateAPIView to allow GET requests
class ContributeCreateView(generics.ListCreateAPIView):
    queryset = Contribute.objects.all()
    serializer_class = ContributeSerializer

    def get(self, request, *args, **kwargs):
       
        cause_id = self.kwargs.get('id')
        
        if cause_id:
          
            contributions = Contribute.objects.filter(causes_id=cause_id)
        else:
           
            contributions = self.get_queryset()
            
        serializer = self.get_serializer(contributions, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        cause_id = self.kwargs.get('id')
        
        if not cause_id:
            cause_id = request.data.get('causes')

        try:
            cause = Causes.objects.get(id=cause_id)
        except (Causes.DoesNotExist, ValueError):
            return Response({
                'message': 'Valid Cause ID is required to contribute'
            }, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        data['causes'] = str(cause_id)
        
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Contribution created successfully',
                'contribution': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)