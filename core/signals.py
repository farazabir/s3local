from django.dispatch import receiver
from .views import file_uploaded, folder_created

@receiver(file_uploaded)
def handle_file_upload(sender, **kwargs):
    file_object = kwargs['file_object']
    print(f"File uploaded: {file_object} in folder {file_object.folder}")

@receiver(folder_created)
def handle_folder_creation(sender, **kwargs):
    folder = kwargs['folder']
    print(f"Folder created: {folder.name}")