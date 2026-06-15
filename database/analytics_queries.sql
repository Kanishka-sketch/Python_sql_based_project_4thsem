--Total problems Solved
SELECT COUNT(*) AS TotalSolved
FROM DSA_Problems;

--Difficulty-wise Count
SELECT difficulty, COUNT(*) AS Count
FROM DSA_Problems
GROUP BY difficulty;

--Completed SQL Topics 

SELECT COUNT(*) AS CompletedTopics
FROM SQL_Practice
WHERE status='Completed';

--Average Mock Score
SELECT AVG(score) AS AverageScore
FROM Mock_Interviews;

--Company Preparation Status
SELECT company_name,status
FROM Companies;

-- Topic Wise Problem Count
SELECT topic, COUNT(*) AS Count
FROM DSA_Problems
GROUP BY topic;