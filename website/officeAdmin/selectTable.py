from sqlalchemy import text
from .config import connection


conn = connection()

def selectTable(column_names,table_names,where_condition):
    qry=f"select {column_names} from {table_names} {where_condition}"
    sql=text(qry)
    try:
        result=conn.execute(sql)
    except:
        print("Error")
        try:
            result=conn.execute(sql)
        except:
            result=conn.execute(sql)
    return result