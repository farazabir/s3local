# s3local


S3 Local is a lightweight Django REST Framework and Docker-based mimicking aws s3 for local development.  
---

## **Features**
- **Folder Creation**: Organize files into folders.
- **File Upload/Download**: Upload and download files with ease.
- **Event Notifications**: Receive notifications for file uploads and folder creation.
- **AWS-like Endpoints**: Use S3-style REST API endpoints (e.g., `/{folder-name}/`).
- **Docker Support**: Run the project locally using Docker.

---

## **Quick Start**

### **Prerequisites**
- Docker and Docker Compose installed.

### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/s3-local.git
   cd s3-local
   ```

2. Build and start the Docker containers:
   ```bash
   docker-compose up --build
   ```

3. Access the API at `http://localhost:8000/s3/`.

---

## **API Endpoints**

### **Create a Folder**
- **Endpoint**: `POST /s3/`
- **Request**:
  ```json
  {
    "name": "my-folder"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "my-folder",
    "created_at": "2023-10-01T12:00:00Z"
  }
  ```

### **Upload a File**
- **Endpoint**: `POST /s3/{folder-name}/`
- **Request**:
  ```bash
  curl -X POST http://localhost:8000/s3/my-folder/ \
       -F "file=@/path/to/your/file.txt" \
       -F "name=file.txt"
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "file.txt",
    "file": "http://localhost:8000/media/files/file.txt",
    "folder": 1,
    "uploaded_at": "2023-10-01T12:05:00Z"
  }
  ```

### **Download a File**
- **Endpoint**: `GET /s3/download/{file-id}/`
- **Request**:
  ```bash
  curl -X GET http://localhost:8000/s3/download/1/ --output downloaded_file.txt
  ```

---
