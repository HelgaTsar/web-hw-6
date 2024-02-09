import sqlite3


def execute_query_9(sql: str) -> list:
    with sqlite3.connect('hw6.db') as conn:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT d.name AS discipline, s.fullname AS student
FROM grades g 
LEFT JOIN disciplines d ON d.id  = g.disciplines_id
LEFT JOIN students s  ON s.id = g.students_id  
WHERE s.id = 23
GROUP BY d.id;
"""

if __name__== '__main__':
    try:
        print(execute_query_9(sql))
    except sqlite3.Error as error:
        print(error)
