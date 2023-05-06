from sqlalchemy import text
from .config import connection


conn = connection()

def updateTable(table_names,column_names,where_condition):
    qry=f"UPDATE {table_names} {column_names} {where_condition};"
    sql=text(qry)
    conn.execute(sql)
    try:
        conn.commit()
        isSuccess=True
    except:
        isSuccess=False
    return isSuccess