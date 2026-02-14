from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from academicRecords.models import AcademicRecord
from academicRecords.serializers import AcademicRecordSerializer

class AcademicRecordListCreateView(APIView):    
    def get(self, request):
        records = AcademicRecord.objects.all().select_related('student', 'graded_by')
        serializer = AcademicRecordSerializer(records, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AcademicRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AcademicRecordDetailView(APIView):    
    def get_object(self, pk):
        try:
            return AcademicRecord.objects.select_related('student', 'graded_by').get(pk=pk)
        except AcademicRecord.DoesNotExist:
            return None
    
    def get(self, request, pk):
        record = self.get_object(pk)
        if not record:
            return Response({"error": "Academic record not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AcademicRecordSerializer(record)
        return Response(serializer.data)
    
    def put(self, request, pk):
        record = self.get_object(pk)
        if not record:
            return Response({"error": "Academic record not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AcademicRecordSerializer(record, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        record = self.get_object(pk)
        if not record:
            return Response({"error": "Academic record not found."}, status=status.HTTP_404_NOT_FOUND)
        
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)