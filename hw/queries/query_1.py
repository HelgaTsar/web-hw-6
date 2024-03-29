import sqlite3


def execute_query_1(sql: str) -> list:
    with sqlite3.connect('hw6.db') as conn:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.fullname, ROUND(AVG(g.grades),2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.students_id
GROUP BY s.fullname 
ORDER BY average_grade DESC 
LIMIT 5;
"""

if __name__== '__main__':
    try:
        print(execute_query_1(sql))
    except sqlite3.Error as error:
        print(error)
