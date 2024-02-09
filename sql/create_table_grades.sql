DROP TABLE IF EXISTS grades; 
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    grades INTEGER, 
    disciplines_id REFERENCES disciplines (id),
    students_id REFERENCES students (id),
    date_of DATE
);