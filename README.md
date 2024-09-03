# Little Lemon

A web application created for an imaginary bistro to:
- Offer a dynamic menu to end-users.
- Book reservations.
- Provide managers with an easy-to-use administration panel.

## Installation

### SQLite version
1. Go to the main branch.
2. Download .zip file or clone the git repository.
3. Create a virtual environment ```python -m venv venv```<br>
4. Activate the virtual environment.<br>
Powershell: ```.\venv\Scripts\activate```<br>
Linux: ```source ./venv/bin/activate```<br>
Then, install django ```python -m pip install django```
5. Go to the root folder of the project.
6. Run the development server ```python ./manage.py runserver```
7. Open your web browser and enter the URL: ```localhost:8000```

### MySQL version
1. Go to the MySQL-version branch.
1. Download .zip file or clone the git repository.
1. Create a virtual environment ```python -m venv venv```<br>
1. Activate the virtual environment.<br>
Powershell: ```.\venv\Scripts\activate```<br>
Linux: ```source ./venv/bin/activate```<br>
Then:<br>
Install django ```python -m pip install django```<br>
Install django-environ ```python -m pip install django-environ```<br>
Install mysqlclient ```python -m pip install mysqlclient```
1. Create an .env file and enter the credentials specified at the .env.example file to create a connection to a MySQL database.
1. Go to the root folder of the project.
1. Make the migrations entering the following commands: ```python ./manage.py makemigrations```<br>
```python ./manage.py migrate```
1. Run the development server ```python ./manage.py runserver```
1. Open your web browser and enter the URL: ```localhost:8000```

## Admin Panel Access
### What is it?
It is an easy-to-use interface provided to manage the application data model.<br>
As a manager, you will be able to:
- Make updates to the offered menu.
- Check the clients reservations.

### How to access?
First, turn on the development server by entering the command: ```python ./manage.py runserver```.<br>
Then, in your web browser enter the following URL: ```localhost:8000/admin```.<br>
To log in, use the following credentials:
- **Name:** bistroadmin
- **Password:** lemon@123<br>
<!-- -->
Now, you will have access to the application data model!