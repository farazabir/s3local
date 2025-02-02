from django.urls import path
from .views import FolderCreateView, FileUploadView, FileDownloadView


urlpatterns = [
    path('<str:folder_name>/', FileUploadView.as_view(), name='file-upload'),
    path('', FolderCreateView.as_view(), name='folder-create'),
    path('download/<int:file_id>/', FileDownloadView.as_view(), name='file-download'),
]

