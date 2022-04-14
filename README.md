# django apps
---

# Marketplace

### Python Packages

```
pip install django python-dot-env mysql-connector-python
```

### Setup MySQL
```
mysql>
source /path/to/classicmodels.sql
```

### .ENV

```
cd djangoapps/marketplace
touch .env
```

.env contents:
```
HOST="localhost"
DB="classicmodels"
USER="root"
PORT="3306"
PASSWORD="enter_your_mysql_password_here"
```

### Run Server

```
cd djangoapps
python3 manage.py runserver localhost:8000
```

Browse to http://localhost:8000 to open application

### Other Notes:

Login Password: `admin12345`


### Directory Structure:

```
.
├── classicmodels.sql
├── db.sqlite3
├── djangoapps
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── marketplace
│   ├── admin.py
│   ├── apps.py
│   ├── db_helper.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── __pycache__
│   ├── templates
│   │   ├── customers.html
│   │   └── login.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── README.md
```