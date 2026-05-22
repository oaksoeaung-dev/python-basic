-- SQLite
CREATE TABLE Location (
    Id TEXT PRIMARY KEY,
    Division TEXT NOT NULL
);

CREATE TABLE Student_Details (
    Id TEXT PRIMARY KEY,
    Student_Name TEXT NOT NULL,
    Township_Id TEXT,
    FOREIGN KEY (Township_Id) REFERENCES Location(Id)
);

CREATE TABLE Course (
    Id TEXT PRIMARY KEY, -- ဥပမာ - C-001, C-002
    Course_Name TEXT NOT NULL,
    Instructor_Name TEXT NOT NULL
);

CREATE TABLE Student_Courses (
    Student_Id TEXT,
    Course_Id TEXT,
    PRIMARY KEY (Student_Id, Course_Id),
    FOREIGN KEY (Student_Id) REFERENCES Student_Details(Id),
    FOREIGN KEY (Course_Id) REFERENCES Course(Id)
);