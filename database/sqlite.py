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
def add_entry(entry: tuple):
    conn = sqlite3.connect('category_master.db')
    add_command = "INSERT INTO taxonomy VALUES ('%s','%s', '%s')" % entry
    try:
        c = conn.cursor()
        c.execute(add_command)
    except Exception as e:
        print(e)


def find_entry(entry: tuple) -> list:
    conn = sqlite3.connect('category_master.db')
    select_command = """
        SELECT FROM taxonomy WHERE concept = '%s' AND part_of_speech = '%s'
    """
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
        CREATE TABLE IF NOT EXISTS taxonomy (
        concept_group TEXT NOT NULL,
        category TEXT NOT NULL,
        part_of_speech TEXT NOT NULL,
        CONSTRAINT PK_Concept PRIMARY KEY (concept_group, category)
        )
    """
    create_table(conn, create_command)



