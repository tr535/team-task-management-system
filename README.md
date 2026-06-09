# Team Task Management System

A role-based task management platform built with Django and SQLite that enables teams to organize, assign, and track tasks efficiently through a secure and structured workflow.

## Key Features

* User authentication and role-based authorization
* Team-based task isolation
* Manager and employee roles
* Task assignment workflow
* Status tracking (New → In Progress → Completed)
* Locked completed tasks
* Personal task filtering ("My Tasks")
* Secure server-side permission checks

## Technologies

- Python
- Django
- SQLite
- Bootstrap 5
- HTML
- CSS

## Business Logic

Managers can create, edit, and delete tasks that have not yet been assigned to employees. Employees can claim available tasks and update their progress through a defined workflow:

**New → In Progress → Completed**

Completed tasks become locked to preserve data integrity and prevent further modifications.

The system enforces team-based access control, ensuring that users can only view and interact with tasks belonging to their own team through secure server-side validation.

### System Screenshots

**Dashboard View:**
![Dashboard](dashbord.png)

**Task Management:**
![Add Task](add-task.png)


## Project Demo

Here is the system in action:

![Workflow Demonstration](gif.gif)



## Getting Started

### Prerequisites

Make sure you have Python installed on your machine.

```bash
python --version
```

### Installation

```bash
git clone https://github.com/tr535/team-task-management-system.git
cd team-task-management-system
pip install -r requirements.txt
```

### Running the Application

```bash
python manage.py migrate
python manage.py runserver
```

Open your browser and navigate to:

```
http://127.0.0.1:8000
```
