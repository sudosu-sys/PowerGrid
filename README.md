# PowerGrid ⚡📊

## Overview 📚
PowerGrid is a Student Grades Management System built with Django to help teachers track and manage student performance across subjects and grade levels. It’s scalable, flexible, and simplifies the grading process.

---

## Tech Stack 🔧
- **Backend:** Django (Python)
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Reporting Tools:** PDFKit, CSV

---

## Features 📋
- **Subject Management 📈:** Supports tracking grades for any subject and grade level.
- **Role-Based Groups 📝:** Teachers are grouped by subject with secure access controls.
- **Student Profiles 👤:** Stores student names and grade levels (9–12).
- **Grade Tracking 📅:** Records grades and calculates averages by subject.
- **Report Generation 📃:** Exports student performance reports as CSV files.
- **Secure Access 🛡️:** Role-based security ensures data privacy.
- **Scalable Design 🌟:** Easily extendable to support more subjects and features.

---

## Problem 🤔
Manual grade tracking is slow, error-prone, and inefficient. Teachers struggle with calculations, reports, and data accuracy.

---

## Solution 💡
PowerGrid automates grade tracking, calculates averages, and generates reports instantly—saving time and reducing errors.

---

## Installation 🛠️
1. Clone the repository:
   ```bash
   git clone https://github.com/sudosu-sys/PowerGrid.git
   ```
2. Go to the project directory:
   ```bash
   cd PowerGrid
   ```
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Apply migrations:
   ```bash
   python manage.py migrate
   ```
6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
7. Start the server:
   ```bash
   python manage.py runserver
   ```

---

## Final Thoughts 🎉
PowerGrid ⚡ simplifies grading and report generation, making teachers' lives easier. Ready to power up your school? Give PowerGrid a try!

---

## License 📄
This project is licensed under the [MIT License](LICENSE).

