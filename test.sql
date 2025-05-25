CREATE TABLE 'Student'
(
'student_id' int,
'name' varchar,
'phone' int(10),
PRIMARY KEY ('student_id')
);

CREATE TABLE 'Result'
(
'student_id' INT,
'module_code' varchar,
'score' INT
);

CREATE TABLE 'Friend'
(
'student_id_1' INT,
'student_id_2' INT
);

INSERT INTO Student
VALUES
(123117795, 'Rajeev', 879828353),
(123117796, 'Sam', 879828354),
(123117797, 'Vladdy', 879828355),
(123117798, 'Harry', 879828356),
(123117799, 'Simon', 879828357)

INSERT into Friend
VALUES
(123117795,123117798),
(123117795,123117799),
(123117796,123117797),
(123117798,123117799),
(123117796,123117799)

INSERT INTO Result
VALUES
(123117795, 'CS8022', 89),
(123117796, 'CS8022', 72),
(123117797, 'CS8022', 63),
(123117798, 'CS8022', 78),
(123117799, 'CS8022', 92)

SELECT Avg(r.score)
FROM Student as s, Friend as f, Result as r
WHERE s.student_id=123117795, f.student_id_1= s.student_id, f.student_id_2=r.student_id