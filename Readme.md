
![Logo](https://img.freepik.com/free-icon/todo-list_318-10185.jpg)


# 📝 **Todo Application**
## Based on
 ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
 ![SqlLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![drf](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![jwt](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)
![postgresql](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)



📌 However, in general, a "todo" application typically refers to a task management system where users can create, update, and manage their tasks or to-do lists. It allows users to add tasks, set due dates, mark tasks as completed, and potentially categorize or prioritize tasks.

🔧 If you are looking to build a todo application using Django Rest Framework, you can start by defining your models for tasks, such as a `Task` model with fields like title, description, due date, and completion status. Then, you can create Django Rest Framework serializers and views to handle CRUD operations (Create, Read, Update, Delete) for tasks.

🔐 To add JWT authentication to your API, you can follow the steps mentioned in the previous response.

🚀 Once your API is set up with authentication, you can integrate it with a frontend application or use tools like cURL or Postman to interact with the API endpoints directly and perform tasks such as creating tasks, retrieving task details, updating tasks, and marking tasks as complete.



## Installation

Clone this repository
   ```
    git clone https://github.com/Deepanshu291/TodoBackend-Django-rest-framework
   ```
Install my-project with pip

```bash
  cd my-project
  pip Install -r requirements.txt
```
Migrate project 
```
  python manage.py makemigrations  
  python manage.py migrate
```  

Run Project 
```
  python manage.py runserver
```  
## Features

- Login/Logout 
- Fast development
- Downlaod Source Code
- Use Custom Input 


## Demo

You can login and use Todo-api from [this link]("https://todoapi29.pythonanywhere.com/") https://todoapi29.pythonanywhere.com/

#### username : deepanshu 
#### password : 1234

### To perform GET, POST Request
```
http://127.0.0.1:8000/api/todo/
```

### To perform  PATCH, DELETE Request
```
http://127.0.0.1:8000/api/todo/<str:uuid>
```

### Admin Panel 

```
http://127.0.0.1:8000/api/admin
```

### POST Request for login , Register User
```
http://127.0.0.1:8000/api/login/
http://127.0.0.1:8000/api/register/
```
### GET Request to Logout
```
http://127.0.0.1:8000/api/logout/
```


## 🚀 About Me
I am a very Enthusiastic Developer to learn new technology like Flutter, MERN, And many more. I Want to see myself as Full Stack Developer in Future.

### 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://deepanshu291.github.io/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/deepanshu291/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/)
## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

