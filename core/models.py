from django.db import models
import os


class Folder(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class FileObject(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

def dynamic_upload_path(instance, filename):
    """Store files dynamically based on the folder name"""
    if instance.folder:
        return os.path.join('s3', instance.folder.name, filename) 
    return os.path.join('s3/default', filename)  
class Folder(models.Model):
    name = models.CharField(max_length=255, unique=True)  

class FileObject(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to=dynamic_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)