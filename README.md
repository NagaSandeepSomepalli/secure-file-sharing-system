```markdown
# 🌟 Secure File-Sharing System: Flask-based Solution

---

## **🎯 Project Overview**

The **Secure File-Sharing System** is a Python-based web application built with the **Flask framework**. This system provides a secure platform for uploading, sharing, and downloading files with features like role-based access, encrypted download links, and email verification.

---

## **✨ Features**

### **Ops User**
- 🔒 **Login**: Secure login functionality.  
- 📂 **File Upload**: Upload files of specific types (*pptx, docx, xlsx*) only.

### **Client User**
- 📝 **Sign Up**: User registration with encrypted email verification.  
- 📧 **Email Verification**: Securely verify email addresses.  
- 🔑 **Login**: Secure access to the system.  
- 📋 **List All Files**: View all files uploaded by the Ops User.  
- 📥 **Download Files**: Retrieve files using secure, encrypted links.

---

## **📂 Project Structure**

```
secure-file-sharing/
│
├── app.py                     # Main application entry point
├── models.py                  # Database models
├── routes/
│   ├── ops_user_routes.py     # Routes for Ops User
│   ├── client_user_routes.py  # Routes for Client User
│   └── utils.py               # Helper functions for encryption, email, etc.
├── uploads/                   # Folder to store uploaded files
├── config.py                  # Configuration settings (e.g., SECRET_KEY)
└── tests/
    └── test_app.py            # Test cases for APIs
```

---

## **🚀 Getting Started**

### **1. Prerequisites**
- ✅ Python 3.8 or higher.
- ✅ Code editor (e.g., VS Code).
- ✅ Required libraries:
  ```bash
  pip install flask flask-restful flask-sqlalchemy flask-mail itsdangerous pytest
  ```

### **2. Run the Application**
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/secure-file-sharing.git
   cd secure-file-sharing
   ```
2. Initialize the database:
   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   ```
3. Start the application:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to `http://127.0.0.1:5000`.

---

## **🔗 API Endpoints**

### **Ops User**
- **Login**:  
  `POST /login` – Logs in the Ops User.  
- **Upload File**:  
  `POST /upload` – Uploads a file (*pptx, docx, xlsx*).

### **Client User**
- **Sign Up**:  
  `POST /signup` – Registers a new client user.  
- **Email Verification**:  
  `GET /verify-email/<token>` – Verifies the email using an encrypted token.  
- **Login**:  
  `POST /login` – Logs in the client user.  
- **List Files**:  
  `GET /list-files` – Lists all files uploaded by Ops Users.  
- **Download File**:  
  `GET /download/<file_id>` – Returns an encrypted URL for file download.

---

## **🧪 Testing**

Test cases are written using **Pytest** and can be found in the `tests/` folder.

### **Run Tests**
```bash
pytest
```

---

## **📦 Deployment**

### **1. Dockerize the Application**
Create a `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```
Build and run the Docker container:
```bash
docker build -t secure-file-sharing .
docker run -p 5000:5000 secure-file-sharing
```

### **2. Deploy to Heroku**
1. Install the Heroku CLI:
   ```bash
   curl https://cli-assets.heroku.com/install.sh | sh
   ```
2. Log in to Heroku:
   ```bash
   heroku login
   ```
3. Create a Heroku app:
   ```bash
   heroku create secure-file-sharing
   ```
4. Push your code to Heroku:
   ```bash
   git push heroku main
   ```

---

## **🤝 Contributions**

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## **📜 License**

This project is licensed under the MIT License. See the `LICENSE` file for details.
```


