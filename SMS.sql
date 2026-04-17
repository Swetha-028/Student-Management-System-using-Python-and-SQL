CREATE DATABASE student_db;
USE student_db;

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    gender VARCHAR(10),
    course VARCHAR(50),
    department VARCHAR(50),
    marks INT,
    attendance INT,
    email VARCHAR(100)
);

SELECT * FROM student_db.students;
