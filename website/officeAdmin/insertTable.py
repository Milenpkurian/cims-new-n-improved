from sqlalchemy import text
from .config import connection


conn = connection()

def insertTable(table_names,column_names,values,where_condition):
    qry=f"INSERT INTO {table_names} {column_names} VALUES {values} {where_condition};"
    sql=text(qry)
    conn.execute(sql)
    try:
        conn.commit()
        isSuccess=True
    except:
        isSuccess=False
    return isSuccess