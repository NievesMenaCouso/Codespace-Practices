
TRUNCATE TABLE student;
TRUNCATE TABLE module;


--Excercise00: Create the table called student with the attributes as shown: studentno, surname, firstname, email. Using the following data dictionary
CREATE TABLE student (
    studentno varchar(10),
    surname varchar(30), 
    firstname varchar(20), 
    email varchar(20), 
	phone int (7) 
);

--Exercise01: Create a table called ‘module’ that has the following attributes – moduleno, modulename, moduleunitsize, hoursfordelivery.
CREATE TABLE module (
    moduleno varchar(10),
    modulename varchar(50),
    moduleunitsize int(3),
    hoursfordelivery int(3)
);

ALTER TABLE module ADD PRIMARY KEY (moduleno); 
  
ALTER TABLE module ADD studentno varchar(10); 

ALTER TABLE module ADD CONSTRAINT FK_module FOREIGN KEY (studentno) REFERENCES student(studentno); 

--Activity 1 -Modifying Data

INSERT INTO student VALUES('EC007','Flintstone','Fred', 'flintstone@bt.com', 1234567);
INSERT INTO student VALUES('EC008','Flintstone','Wilma', 'w.flintstone@bt.com', 2345678),('EC009','Flintstone','Dino', 'd.flintstone@bt.com', 3456789);

--Exercise03: Insert into this table the following record
INSERT INTO module VALUES('DH3J34','SQL: Introduction',1, 32, 'EC007');

--Exercise04: Use code to alter the value from Fred to Barney
UPDATE student SET firstname = 'Barney' WHERE firstname = 'Fred';

--Exercise04: Return the value and put it back to Fred

SELECT * FROM student;

UPDATE student SET firstname = 'Fred' WHERE firstname = 'Barney';

SELECT * FROM student;

--Exercise05: do sql that will show Barney and the module details – using a join.

UPDATE student SET firstname = 'Barney' WHERE firstname = 'Fred'; 
 
SELECT surname, firstname,email, phone, student.studentno, modulename
FROM student, module
WHERE student.studentno = module.studentno AND firstname = 'Barney';

