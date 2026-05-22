
INSERT INTO Location (Id, Division) VALUES ('Kamayut', 'Yangon');
INSERT INTO Location (Id, Division) VALUES ('Hlaing', 'Yangon');
INSERT INTO Location (Id, Division) VALUES ('Chanayethazan', 'Mandalay');

INSERT INTO Student_Details (Id, Student_Name, Township_Id) VALUES ('STU-001', 'Aung Aung', 'Kamayut');
INSERT INTO Student_Details (Id, Student_Name, Township_Id) VALUES ('STU-002', 'Su Su', 'Hlaing');
INSERT INTO Student_Details (Id, Student_Name, Township_Id) VALUES ('STU-003', 'Kyaw Kyaw', 'Chanayethazan');

INSERT INTO Course (Id, Course_Name, Instructor_Name) VALUES ('C-001', 'PHP', 'U Ba');
INSERT INTO Course (Id, Course_Name, Instructor_Name) VALUES ('C-002', 'C#', 'Daw Hla');
INSERT INTO Course (Id, Course_Name, Instructor_Name) VALUES ('C-003', 'Java', 'U Ba');
INSERT INTO Course (Id, Course_Name, Instructor_Name) VALUES ('C-004', 'Python', 'U Mya');

INSERT INTO Student_Courses (Student_Id, Course_Id) VALUES ('STU-001', 'C-001');
INSERT INTO Student_Courses (Student_Id, Course_Id) VALUES ('STU-001', 'C-002');
INSERT INTO Student_Courses (Student_Id, Course_Id) VALUES ('STU-001', 'C-003');
INSERT INTO Student_Courses (Student_Id, Course_Id) VALUES ('STU-002', 'C-002');
INSERT INTO Student_Courses (Student_Id, Course_Id) VALUES ('STU-002', 'C-004');
INSERT INTO Student_Courses (Student_Id, Course_Id) VALUES ('STU-003', 'C-003');