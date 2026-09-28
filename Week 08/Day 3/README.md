# WEEK 08 — DAY 03
## Course Registration Database

> Designing a simple database structure before writing Django models.

---

## 🎯 Mission of the Day

Today, I practiced the basic structure of a course registration database.

The goal was to understand how data is organized into entities, how tables are connected, and how relationships work in a relational database.

---

## 🧭 What I Practiced

| Step | Topic | What I Practiced |
|------|-------|------------------|
| 01 | Entities | Student, Course, Enrollment |
| 02 | Primary Keys | Identifying each table uniquely |
| 03 | Attributes | Adding useful data to Student and Course |
| 04 | Foreign Keys | Connecting Enrollment to Student and Course |
| 05 | Relationships | Understanding one-to-many relationships |
| 06 | Many-to-Many | Breaking Student ↔ Course into two relationships |
| 07 | Constraints | Using UNIQUE and NOT NULL |
| 08 | Database Diagram | Drawing and connecting the three tables |

---

## 🗂️ Database Entities

### 👤 Student

Represents a person who can register for courses.

**Primary Key:**  
`student_id`

**Attributes:**
- `name`
- `email`
- `program`

---

### 📚 Course

Represents a class that students can register for.

**Primary Key:**  
`course_id`

**Attributes:**
- `title`
- `capacity`
- `instructor`

---

### 📝 Enrollment

Represents one student's registration in one course.

**Primary Key:**  
`enrollment_id`

**Foreign Keys:**
- `student_id` → `Student.student_id`
- `course_id` → `Course.course_id`

**Additional Attribute:**
- `enrolled_at`

---

## 🔑 Primary Keys

A Primary Key uniquely identifies each row in a table.

| Table | Primary Key |
|-------|-------------|
| Student | `student_id` |
| Course | `course_id` |
| Enrollment | `enrollment_id` |

A Primary Key cannot be repeated or empty.

---

## 🔗 Foreign Keys

Foreign Keys connect related tables.

The `Enrollment` table contains:

- `student_id` → references `Student.student_id`
- `course_id` → references `Course.course_id`

This allows each enrollment to be connected to the correct student and course.

---

## 🔄 Relationships

### Student → Enrollment

One student can have many enrollments.

**Relationship:**  
`One-to-Many (1:N)`

### Course → Enrollment

One course can have many enrollments.

**Relationship:**  
`One-to-Many (1:N)`

Together, these relationships represent the many-to-many relationship between students and courses.

---

## 🛡️ Constraints

### UNIQUE

`Student.email`

Each student's email should be unique.

### NOT NULL

`Course.title`

A course must have a title.

---

## 🗺️ Database Structure

```text
STUDENT
-----------------
student_id (PK)
name
email (UNIQUE)
program
       |
       | 1
       |
       | M
ENROLLMENT
-----------------
enrollment_id (PK)
student_id (FK)
course_id (FK)
enrolled_at
       |
       | M
       |
       | 1
COURSE
-----------------
course_id (PK)
title (NOT NULL)
capacity
instructor
```

---

## 🧠 Key Takeaway

The `Enrollment` table is a separate entity because students can register for many courses, and each course can have many students.

Instead of repeatedly storing the student's name and course title, `Enrollment` stores `student_id` and `course_id` as Foreign Keys.

This reduces duplication and keeps the original Student and Course records as the single source of truth.

---

## 📝 Exit Ticket

**Why should Enrollment store student_id and course_id instead of repeating the student's name and course title?**

Because `student_id` and `course_id` reference the original Student and Course records.

This avoids duplicated data and reduces the risk of inconsistent information when a student's or course's details are updated.

---

## 💡 What I Learned

- How to identify database entities.
- How to choose Primary Keys.
- How Foreign Keys connect tables.
- How one-to-many relationships work.
- How a many-to-many relationship can be represented using an Enrollment table.
- How to apply UNIQUE and NOT NULL constraints.
- How to represent a database structure using a table diagram.

---

## ✅ Day 03 Complete

**Course Registration Database — Completed**

- [x] Entities identified
- [x] Primary Keys defined
- [x] Attributes added
- [x] Foreign Keys connected
- [x] Relationships defined
- [x] Constraints applied
- [x] Database diagram completed
- [x] Exit Ticket answered
