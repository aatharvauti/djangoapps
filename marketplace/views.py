from django.http import HttpResponse
from django.shortcuts import render

from .db_helper import DBHelper

import hashlib as sh

def customers_list(request):
    
    # get form data from HTML page
    form_data = request.POST

    employee_email = form_data['email']
    employee_password = form_data['password']
    employee_password = sh.sha256(employee_password.encode('utf-8')).hexdigest()

    # init helper
    db_helper = DBHelper()

    # fetch employee details from the database using email
    query_empdetails = "SELECT firstName, lastName, employeeNumber FROM employees WHERE email = %s AND password = %s;"
    params = (employee_email, employee_password)
    employee_details = db_helper.execute_select_query(query_empdetails, params)

    if len(employee_details) == 0:
        return HttpResponse("Invalid Username or Password")

    employee_number = employee_details[0]['employeeNumber']
    first_name = employee_details[0]['firstName']
    last_name = employee_details[0]['lastName']

    # query to list customers
    query_listcustomers = "SELECT customerName, city, country, creditLimit FROM customers WHERE salesRepEmployeeNumber = '%s';"
    params = (employee_number, )
    list_customers = db_helper.execute_select_query(query_listcustomers, params)

    # render data to customers.html
    render_data = {
        "username": first_name + " " + last_name,
        "list_of_customers": list_customers
    }
    return render(request, 'customers.html', render_data)

def login(request):
    return render(request, 'login.html')