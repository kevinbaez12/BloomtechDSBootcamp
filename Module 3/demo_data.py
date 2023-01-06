import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
cursor = conn.cursor()


def execute_query(conn, query):
    '''doc'''
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def modify_table(conn, query):
    '''doc'''
    curs = conn.cursor()
    curs.execute(query)
    conn.commit()


new_table = '''CREATE TABLE "demo"
                        ("S" VARCHAR(10) NOT NULL,
                        "X" INT NOT NULL,
                        "Y" INT NOT NULL
                        );'''

modify_table(conn, new_table)
list1 = ['g', 'v', 'f']
list2 = [3, 5, 8]
list3 = [9, 7, 7]

for i, _ in enumerate(list1):
    modify_table(conn, f'''INSERT INTO demo ("S","X","Y")
                        VALUES ('{list1[i]}','{list2[i]}','{list3[i]}')''')

row_count = '''SELECT COUNT(*) FROM demo'''
xy_at_least_5 = '''SELECT COUNT(*) FROM demo WHERE X>=5
                    AND Y>=5'''
unique_y = '''SELECT COUNT( DISTINCT Y) FROM demo'''