
# 📚 Library Management System (LMS) in Django

A simple Django-based Library Management System where users can:
- Browse books
- Track borrowed books
- Admin can manage books & users

## 🚀 Setup Instructions

1. Clone repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/django-lms.git
   cd django-lms
````

2. Create virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate # Mac/Linux
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start server:

   ```bash
   python manage.py runserver
   ```

👉 Visit [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🛠 Tech Stack

* Python 3.12
* Django 5.x
* SQLite3

````

---

## 🔹 Step 6: Freeze Requirements
Before final push, save your dependencies:

```powershell
pip freeze > requirements.txt
git add requirements.txt README.md .gitignore
git commit -m "Added requirements, README, gitignore"
git push
````

---

✅ Done! Your LMS is now live on GitHub 🎉

