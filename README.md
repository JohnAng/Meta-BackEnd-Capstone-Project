# Capstone Project - Meta Back-End Developer Professional Certificate
---

## How to run the project
* Make sure you have Python, pip and pipenv installed
* Open the terminal and check what python version you have installed by running "python --version"
* Open the Pipfile and check the required version
* Run in terminal ```"pipenv shell"```
* Run in terminal ```"pipenv install"```
* Run in terminal ```"python manage.py runserver"```
* Open the browser in http://127.0.0.1:8000/

---

## API endpoints
* admin/
* restaurant/ [name='index']
* restaurant/menu/
* restaurant/menu/<int:pk>
* restaurant/booking/
* restaurant/booking/tables
* restaurant/booking/tables/<int:pk>
* auth/users/
* auth/users/me/
* auth/users/confirm/
* auth/users/resend_activation/
* auth/users/set_password/
* auth/users/reset_password/
* auth/users/reset_password_confirm/
* auth/users/set_username/
* auth/users/reset_username/
* auth/users/reset_username_confirm/
* auth/token/login/ (Token Based Authentication)
* auth/token/logout/ (Token Based Authentication)
* auth/
* api-token-auth/
  
---

## Be aware
* Check the settings.py file for the DB configuration
* Create a superuser so you can be able to use the admin panel with ```"python manage.py createsuperuser"```
* The API has some token based authentication with Djoser
* Use the proper API endpoints to create a user get a token and login to a user or just make a superuser
  
---

## Landing Page

![Landing page](./README%20IMAGES/landing_page1.jpg)
![Landing page](./README%20IMAGES/landing_page2.jpg)

---

## Browsable API

![browsableAPI](./README%20IMAGES/browsableAPI1.jpg)
![browsableAPI](./README%20IMAGES/browsableAPI2.jpg)
![browsableAPI](./README%20IMAGES/browsableAPI3.jpg)
![browsableAPI](./README%20IMAGES/browsableAPI4.jpg)
![browsableAPI](./README%20IMAGES/browsableAPI5.jpg)
![browsableAPI](./README%20IMAGES/browsableAPI6.jpg)
