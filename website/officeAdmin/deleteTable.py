from sqlalchemy import text
from .config import connection


conn = connection()

def deleteTable(table_names,where_condition):
    qry=f"delete from {table_names} where {where_condition};"
    sql=text(qry)
    conn.execute(sql)
    try:
        conn.commit()
        isSuccess=True
    except:
        isSuccess=False
    return isSuccess