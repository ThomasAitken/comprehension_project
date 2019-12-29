import sqlite3

def create_table(conn, sql_command: str):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_command)
    except Exception as e:
        print(e)

def add_entry(conn, entry: tuple):
    concept = entry[0]
    cat = entry[1]
    add_command = "INSERT INTO taxonomy VALUES ('{}','{}')".format(concept, cat)
    try:
        c = conn.cursor()
        c.execute(add_command)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    conn = sqlite3.connect('category_master.db')
    create_command = """
        CREATE TABLE IF NOT EXISTS taxonomy (
        concept TEXT PRIMARY KEY,
        category TEXT,
        part of speech TEXT NOT NULL
        )
    """
    create_table(conn, create_command)



