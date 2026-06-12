CREATE database InterviewTracker;

use InterviewTracker;

CREATE TABLE Users(
    user_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    college VARCHAR(100)
);

CREATE TABLE DSA_Problems(
    problem_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT,
    problem_name VARCHAR(100) NOT NULL,
    difficulty VARCHAR(20),
    topic VARCHAR(50),
    platform VARCHAR(50),
    date_solved DATE,

    FOREIGN KEY (user_id)
    REFERENCES Users(user_id)
);

CREATE TABLE SQL_Practice(
    sql_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT,
    topic VARCHAR(100),
    difficulty VARCHAR(20),
    practice_date DATE,
    status VARCHAR(20),

    FOREIGN KEY (user_id)
    REFERENCES Users(user_id)
);

CREATE TABLE Companies(
    company_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT,
    company_name VARCHAR(100),
    status VARCHAR(20),
    notes VARCHAR(500),

    FOREIGN KEY (user_id)
    REFERENCES Users(user_id)
);

CREATE TABLE Mock_Interviews(
    mock_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT,
    mock_date DATE,
    score INT,
    feedback VARCHAR(500),

    FOREIGN KEY (user_id)
    REFERENCES Users(user_id)
);