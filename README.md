# Team Task Management System

A full-stack task management system built with Django and SQLite, designed for teams to organize, assign, and track tasks through a secure role-based workflow with team isolation and server-side authorization.

---

## Key Features

- User authentication and role-based authorization
- Team-based task isolation
- Manager and employee roles
- Task assignment workflow
- Status tracking (**New → In Progress → Completed**)
- Locked completed tasks
- Personal task filtering ("My Tasks")
- Secure server-side permission checks

---

## Technologies

### Backend

- Python
- Django
- SQLite

### Frontend

- HTML
- CSS
- Bootstrap 5

---

## Business Logic

Managers can create, edit, and delete tasks that have not yet been assigned to employees. Employees can claim available tasks and update their progress through a structured workflow.

**Workflow**

```
New
   ↓
In Progress
   ↓
Completed
```

Completed tasks become read-only to preserve data integrity and prevent further modifications.

The application enforces strict team-based access control, ensuring that users can only view and interact with tasks belonging to their own team through secure server-side validation—even if requests or URLs are manipulated manually.

---

## 🎥 Project Demo

<p align="center">
  <img src="./gif.gif" width="900" alt="Workflow Demonstration"/>
</p>

---

## 📸 System Screenshots

<table>
<tr>
<td align="center">

**Dashboard**

<img src="./dashbord.png" width="450"/>

</td>

<td align="center">

**Task Management**

<img src="./add-task.png" width="450"/>

</td>
</tr>
</table>

---

## Getting Started

### Prerequisites

Make sure you have **Python** installed on your machine.

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

### Open the Application

Visit:

```text
http://127.0.0.1:8000
```

---

## Project Highlights

- Role-based access control for managers and employees
- Team isolation with secure server-side validation
- Task ownership and assignment workflow
- Business rules preventing completed tasks from being modified
- Clean Django architecture using models, forms, views, and authentication
