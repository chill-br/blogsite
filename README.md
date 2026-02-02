
# 📝 Vichar – Django Blog Application

Vichar is a simple and clean blog web application built using **Django**.  
It allows users to register, log in, create blog posts with images, and view blogs in a card-based layout.

---

## 🚀 Features

- 🔐 User Authentication (Register, Login, Logout)
- ✍️ Create Blog Posts (Title, Content, Image)
- 🖼 Image Upload Support
- 🗂 Blogs Displayed in Card Format
- 👤 Blog Ownership
  - Edit & Delete allowed **only for Admin and Blog Author**
- 📅 Blog timestamp and author details
- 📱 Responsive and modern UI

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **Database:** SQL
- **Authentication:** Django Auth System
- **Media Handling:** Django Media Files

---

## 📂 Project Structure

```

blogsite/
│
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── create.html
│   │   ├── edit.html
│   │   └── post_detail.html
│   ├── static/
│   │   └── blog/styles.css
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── blogsite/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/
├── db.sqlite3
└── manage.py

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/chill-br/blogsite.git
cd blogsite
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install django pillow
```

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6️⃣ Run Server

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

---

## 🔑 User Permissions

| Action      | Who Can Do It       |
| ----------- | ------------------- |
| View Blogs  | Everyone            |
| Create Blog | Logged-in Users     |
| Edit Blog   | Blog Author / Admin |
| Delete Blog | Blog Author / Admin |

---

## 📸 Screenshots (Optional)

<img width="1918" height="865" alt="image" src="https://github.com/user-attachments/assets/5e9b118f-05db-4c7e-a38d-686d59932938" />
<img width="1918" height="870" alt="image" src="https://github.com/user-attachments/assets/5ac21115-62e1-4b5b-834b-b3ecdf95418e" />

---

## 🎯 Future Improvements

* Like & Comment system
* Pagination
* Search functionality
* Categories & tags
* Deployment (Render / Railway / PythonAnywhere)

---

## 👨‍💻 Author

**Ajay**
B.Tech in Artificial Intelligence & Machine Learning

* GitHub: [https://github.com/chill-br](https://github.com/chill-br)

---

## 📄 License

This project is for learning and educational purposes.

```




