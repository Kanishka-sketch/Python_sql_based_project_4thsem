use InterviewTracker;

INSERT INTO Users(name,email,college)
VALUES
('Darshil','darshil@gmail.com','XYZ Engineering College');

select * from Users;

INSERT INTO DSA_Problems (user_id, problem_name, difficulty, topic, platform, date_solved) VALUES
(1, 'Two Sum', 'Easy', 'Array', 'LeetCode', '2026-05-20'),
(1, 'Valid Parentheses', 'Easy', 'Stack', 'LeetCode', '2026-05-21'),
(1, 'Merge Intervals', 'Medium', 'Array', 'LeetCode', '2026-05-23'),
(1, 'Binary Tree Level Order Traversal', 'Medium', 'Tree', 'LeetCode', '2026-05-25'),
(1, 'LRU Cache', 'Hard', 'Design', 'LeetCode', '2026-05-28'),
(1, 'Reverse Linked List', 'Easy', 'Linked List', 'GeeksforGeeks', '2026-05-29'),
(1, 'Longest Substring Without Repeating Characters', 'Medium', 'String', 'LeetCode', '2026-06-01'),
(1, 'Kth Largest Element in an Array', 'Medium', 'Heap', 'LeetCode', '2026-06-03'),
(1, 'Word Break', 'Hard', 'Dynamic Programming', 'LeetCode', '2026-06-05'),
(1, 'Number of Islands', 'Medium', 'Graph', 'LeetCode', '2026-06-08'),
(1, 'Maximum Subarray', 'Medium', 'Array', 'LeetCode', '2026-06-09'),
(1, 'Climbing Stairs', 'Easy', 'Dynamic Programming', 'LeetCode', '2026-06-09'),
(1, 'Valid Anagram', 'Easy', 'String', 'LeetCode', '2026-06-10'),
(1, 'Binary Search', 'Easy', 'Array', 'LeetCode', '2026-06-10'),
(1, 'Course Schedule', 'Medium', 'Graph', 'LeetCode', '2026-06-11'),
(1, 'Trapping Rain Water', 'Hard', 'Array', 'LeetCode', '2026-06-11'),
(1, 'Lowest Common Ancestor of a BST', 'Medium', 'Tree', 'LeetCode', '2026-06-12'),
(1, 'Detect Cycle in Linked List', 'Medium', 'Linked List', 'GeeksforGeeks', '2026-06-12'),
(1, 'Top K Frequent Elements', 'Medium', 'Heap', 'LeetCode', '2026-06-13'),
(1, 'Coin Change', 'Hard', 'Dynamic Programming', 'LeetCode', '2026-06-13'),
(1, 'Implement Trie (Prefix Tree)', 'Hard', 'Design', 'LeetCode', '2026-06-14'),
(1, 'Group Anagrams', 'Medium', 'String', 'LeetCode', '2026-06-14');

select * from DSA_Problems;

-- ===== SQL Practice (10 records) =====
INSERT INTO SQL_Practice (user_id, topic, difficulty, practice_date, status) VALUES
(1, 'Joins', 'Easy', '2026-05-20', 'Completed'),
(1, 'Subqueries', 'Medium', '2026-05-22', 'Completed'),
(1, 'CTE (Common Table Expressions)', 'Medium', '2026-05-25', 'Completed'),
(1, 'Window Functions', 'Hard', '2026-05-29', 'In Progress'),
(1, 'Indexes & Query Optimization', 'Hard', '2026-06-02', 'Not Started'),
(1, 'Stored Procedures', 'Medium', '2026-06-06', 'Not Started'),
(1, 'Aggregate Functions (GROUP BY, HAVING)', 'Easy', '2026-06-08', 'Completed'),
(1, 'Normalization (1NF, 2NF, 3NF)', 'Medium', '2026-06-09', 'Completed'),
(1, 'Views and Triggers', 'Medium', '2026-06-11', 'In Progress'),
(1, 'Transactions & ACID Properties', 'Hard', '2026-06-13', 'Not Started');

select * from SQL_Practice;

-- ===== Companies (9 records) =====
INSERT INTO Companies (user_id, company_name, status, notes) VALUES
(1, 'TCS', 'Completed', 'Cleared aptitude and technical round; focused on SQL and basic OOP'),
(1, 'Infosys', 'In Progress', 'Revising DBMS and OS concepts for upcoming technical round'),
(1, 'Accenture', 'Not Started', 'Need to review company profile and recent placement pattern'),
(1, 'Wipro', 'In Progress', 'Practicing aptitude tests; coding round scheduled next week'),
(1, 'Cognizant', 'Not Started', 'Plan to start preparation after Infosys round is done'),
(1, 'Capgemini', 'Completed', 'Cleared online assessment and HR round'),
(1, 'Tech Mahindra', 'In Progress', 'Preparing for group discussion round'),
(1, 'HCL Technologies', 'Not Started', 'Will start after current company rounds finish'),
(1, 'IBM', 'In Progress', 'Reviewing cloud computing basics for technical round');



-- ===== Mock Interviews (7 records) =====
INSERT INTO Mock_Interviews (user_id, mock_date, score, feedback) VALUES
(1, '2026-05-22', 65, 'Need to improve OOP concepts and explain answers more clearly'),
(1, '2026-05-29', 72, 'Good improvement in SQL; work on time complexity explanations'),
(1, '2026-06-05', 78, 'Strong DSA fundamentals; be more confident while explaining approach'),
(1, '2026-06-10', 84, 'Well prepared overall; minor improvement needed in project explanation'),
(1, '2026-06-12', 80, 'Solid problem-solving approach; explain edge cases more proactively'),
(1, '2026-06-14', 88, 'Excellent communication and technical depth this round'),
(1, '2026-06-15', 82, 'Good performance; revise system design basics before next round');
