# Student Management System

A menu-driven Python program to manage student records — built as a course assignment to demonstrate variables, conditions, loops, functions, lists, dictionaries, and file handling.

**Name:** Abdul Wahid
**Reg No:** B25F0416AI290

## Features

- **Add Student** — enter ID, name, age, course, and marks for 3 subjects
- **View All Students** — displays every record along with each student's average marks
- **Search Student** — find a student by ID
- **Update Student** — edit name, age, course, or marks (leave a field blank to keep it unchanged)
- **Delete Student** — remove a student record, with a confirmation prompt
- **Class Statistics** — calculates class average, highest average, lowest average, and the top-performing student

## How it works

- Each student record is stored as a dictionary with keys: `id`, `name`, `age`, `course`, `marks`
- All records are kept in a list while the program runs
- Records are saved to `students.txt` so data persists between runs (file handling)
- The main menu loop uses `if-elif-else` for navigation and runs until the user chooses Exit
- Each feature (add, view, search, update, delete, statistics) is written as its own function

## How to run

```bash
python student_management.py
```

Then follow the on-screen menu (options 1–7).

## Example menu

```
========== Student Management System ==========
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Show Class Statistics
7. Exit
==================================================
```

## Screenshots

*(Add screenshots of the program running here)*
