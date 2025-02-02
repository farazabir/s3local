from rest_framework import serializers
from .models import Folder, FileObject
from django.conf import settings

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ['id', 'name']

class FileObjectSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = FileObject
        fields = ['id', 'file', 'uploaded_at', 'file_url']

    def get_file_url(self, obj):
        request = self.context.get("request")
        if request:
            return request.build_absolute_uri(obj.file.url)
        return obj.file.url