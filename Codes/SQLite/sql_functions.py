import sqlite3
# CRUD create,retrive,update and delete

def insert(conn,table_name,*values):
    (b,*a)= values
    print(a)
    
    #conn.execute(f"""INSERT INTO {table_name} VALUES({values});
    #""")

insert(1,2,54,'chinmayh','hello')