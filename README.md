# Documentation for EliteFreelancer

## Installation Guide

```bash
git clone https://github.com/Versedcamel153/django-restauth-boilerplate.git

cd RestAuth
```

### Create and activate virtual environment
```bash
python manage.py -m venv .venv

source .venv/scripts/actviate/
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Start server
```bash
python manage.py runserver
```

## API Endpoints
### Base URL: `api/v1/auth/`

|Endpoints      | Method |   Details     |
----------------|--------|---   
|`registration/` | POST |  Create a new user
| `login/`        | POST |  Login a user
| `logout/`       | POST |  Logout a user
| `user/`         | GET  | Get user details
| `password/reset/`| POST |  Request a password reset
| `password/reset/confirm/`| POST |  Setup new password after reset request
| `google/`       | POST |  Login/ Signup with Google OAuth
-----------------------------------

## 1. Registration
### Method: `POST`
### URL: `api/v1/auth/registration/`
### Request Body:
```
{
    "username": "",
    "email": "",
    "password1": "",
    "password2": ""
}
```

### Response: `201 Created`
### Response Body:
```
{
    "access": "",
    "refresh": "",
    "user": {
        "pk": 1,
        "email": "",
        "first_name": "",
        "last_name": ""
    }
}
```

## 2. Login
### Method: `POST`
### URL: `api/v1/auth/login/`
### Request Body:
```
{
    "email": "",
    "password": ""
}
```

### Response: `200 OK`
### Response Body:
```
{
    "access": "",
    "refresh": "",
    "user": {
        "pk": 2,
        "email": "unjawned@gmail.com",
        "first_name": "",
        "last_name": ""
    }
}
```


## 3. Logout
### Method: `POST`
### URL: `api/v1/auth/logout/`
### Request Body:
No Request Body

### Response: `200 Ok`


## 4. User details
### Method: `GET`
### URL: `api/v1/auth/user/`
### Request Boody:
No Request Body
### Response: `200 OK`
### Response Body:
```
{
    "access": "",
    "refresh": "",
    "user": {
        "pk": 1,
        "email": "",
        "first_name": "",
        "last_name": ""
    }
}
```


## 5. Request Password Reset
### Method: `POST`
### URL: `api/v1/auth/password/reset/`
### Request Body:
```
{
    "email": ""
}
```

### Response: `200 OK`
### Response Body:
```
{
    "detail": "Password reset e-mail has been sent."
}
```


## 6. Password Reset
### Method: `POST`
### URL: `api/v1/auth/password/reset/confirm/`
### Request Body:
```
{
    "new_password1": "",
    "new_password2": "",
    "uid": "",
    "token": ""
}
```

### Response `200 OK`
### Response Body
```
{
    "detail": "Password has been reset with the new password."
}
```


## 7. Google Login
### Method: `POST`
### URL: `api/v1/auth/google/`
### Request Body:
```
{
    "access_token": "",
    "code": "",
    "id_token": ""
}
```
## Note: 
Only **access_token** is needed in his request the rest are optional.

### Response: `200 OK`
### Response Body: 
```
{
    "access": "",
    "refresh": "",
    "user": {
        "pk": 1,
        "email": "",
        "first_name": "",
        "last_name": ""
    }
}
```

