import sqlite3

#part of speech for nouns include plural-class, i.e. count or mass
#part of speech for verbs include transitivity 

#obviously, many collections of letters will map to multiple 'concept' entries. 
#simple example is "love" which, at the very least, would have two entries for the verb and noun concept

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

#entry tuple with three parts 
def add_entry(entry: tuple, table_name: str):
    conn = sqlite3.connect('category_master.db')
    if table_name == "nouns":
        add_command = "INSERT INTO nouns VALUES ('%s','%s', '%s', '%s')" % entry
    else:
        pass
    try:
        c = conn.cursor()
        c.execute(add_command)
    except Exception as e:
        print(e)


def find_entry(entry: tuple, table_name: str) -> list:
    conn = sqlite3.connect('category_master.db')
    if table_name == "nouns":
        select_command = "SELECT FROM nouns WHERE name = '%s' AND category = '%s'" % entry
    else:
        select_command = "SELECT FROM verbs WHERE name = '%s' AND category = '%s' AND CLASS = '%s'" % entry
    try:
        c = conn.cursor()
        c.execute(select_command)
        rows = c.fetchall()
        return rows
    except Exception as e:
        print(e)
        return []


if __name__ == "__main__":
    conn = sqlite3.connect('category_master.db')
    create_command = """
        CREATE TABLE IF NOT EXISTS nouns (
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        similarity_vector TEXT NOT NULL,
        atomic_sim_vector TEXT NOT NULL,
        CONSTRAINT PK_Concept PRIMARY KEY (name, category)
        )
    """
    create_table(conn, create_command)



