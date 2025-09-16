📝 Django To-Do App
-------------------------------------------------------------------

A simple To-Do List application built with Django.
It allows users to sign up, log in, add, update, and delete tasks.

🚀 Features
-------------------------------------------------------------------
User authentication (signup, login, logout)

Add new tasks

View all tasks

Update task title

Delete tasks

Responsive UI with CSS & FontAwesome icons


⚙️ Installation & Setup
-------------------------------------------------------------------

1. Clone the repository
   ------------------------------------
git clone https://github.com/yourusername/todo-app.git
cd todo-app

2. Create & activate virtual environment
 -------------------------------------------------
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install dependencies
 --------------------------------------------
pip install -r requirements.txt

4. Apply migrations
 --------------------------------------
python manage.py migrate

5. Run the development server
--------------------------------------------
python manage.py runserver


Open your browser at 👉 http://127.0.0.1:8000


🖼️ Screenshots
---------------------------
Dashboard: View, Add, Update, Delete tasks

Login/Signup: User authentication

🛠️ Tech Stack
--------------------------------
Backend: Django

Frontend: HTML, CSS, FontAwesome

Database: SQLite (default, can switch to MySQL/PostgreSQL)

