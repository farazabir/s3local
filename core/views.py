import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from s3local import settings
from .models import Folder, FileObject
from .serializers import FolderSerializer, FileObjectSerializer
from django.dispatch import Signal

file_uploaded = Signal()
folder_created = Signal()

class FolderCreateView(APIView):
    def post(self, request):
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            folder = serializer.save()

            folder_path = os.path.join(settings.MEDIA_ROOT, folder.name)
            os.makedirs(folder_path, exist_ok=True)
            folder_created.send(sender=self.__class__, folder=folder)
            
            response_data = serializer.data
            response_data['folder_path'] = folder_path

            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileUploadView(APIView):
    def post(self, request, folder_name=None):
        print(f"Folder name from URL: {folder_name}")  # Debug: Check folder_name
        print(f"Request FILES: {request.FILES}")  # Debug: Check uploaded files

        if not folder_name:
            return Response({"error": "Folder name is required"}, status=status.HTTP_400_BAD_REQUEST)

        folder, created = Folder.objects.get_or_create(name=folder_name)
        print(f"Folder object: {folder}")  # Debug: Check folder object

        uploaded_file = request.FILES.get('file')
        if not uploaded_file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        file_object = FileObject.objects.create(file=uploaded_file, folder=folder)
        file_uploaded.send(sender=self.__class__, file_object=file_object)

        return Response(
            FileObjectSerializer(file_object, context={"request": request}).data,
            status=status.HTTP_201_CREATED
        )


    


class FileDownloadView(APIView):
    def get(self, request, file_id):
        try:
            file_object = FileObject.objects.get(id=file_id)
            file_path = file_object.file.path
            with open(file_path, 'rb') as file:
                response = Response(file.read(), content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="{file_object.name}"'
                return response
        except FileObject.DoesNotExist:
            return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)
    