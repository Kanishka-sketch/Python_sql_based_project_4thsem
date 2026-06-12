use InterviewTracker;

INSERT INTO Users(name,email,college)
VALUES
('Darshil','darshil@gmail.com','XYZ Engineering College');

select * from Users;

INSERT INTO DSA_Problems
(user_id,problem_name,difficulty,topic,platform,date_solved)
VALUES
(1,'Two Sum','Easy','Array','LeetCode','2025-06-10'),
(1,'Valid Parentheses','Easy','Stack','LeetCode','2025-06-10'),
(1,'Merge Intervals','Medium','Array','LeetCode','2025-06-11'),
(1,'LRU Cache','Hard','Design','LeetCode','2025-06-12');

select * from DSA_Problems;

INSERT INTO SQL_Practice
(user_id,topic,difficulty,practice_date,status)
VALUES
(1,'Joins','Easy','2025-06-10','Completed'),
(1,'Subqueries','Medium','2025-06-11','Completed'),
(1,'CTE','Medium','2025-06-12','In Progress');

select * from SQL_Practice;

INSERT INTO Companies
(user_id,company_name,status,notes)
VALUES
(1,'TCS','Completed','Aptitude and SQL'),
(1,'Infosys','In Progress','DBMS Revision'),
(1,'Accenture','Not Started','');

INSERT INTO Mock_Interviews
(user_id,mock_date,score,feedback)
VALUES
(1,'2025-06-10',70,'Need improvement in OOP'),
(1,'2025-06-11',75,'Good SQL knowledge'),
(1,'2025-06-12',80,'Strong DSA basics');