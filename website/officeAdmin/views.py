from flask import Blueprint, render_template, request, flash, jsonify,redirect,url_for, make_response
from flask_login import login_required, current_user
from sqlalchemy import exc, create_engine, text,func
from .selectTable import selectTable
from .insertTable import insertTable
from .updateTable import updateTable
from .deleteTable import deleteTable
from datetime import date as dt,datetime
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    return render_template("/home/dashboard.html", user=current_user)

@views.route('/<id>',methods=['GET','POST'])
@login_required
def stock_details(id):
    timestamp = datetime.now()
    if id=="Lab Items":
        item_type=""" (d.item_type LIKE '%Chemical%' OR 
            d.item_type = 'Equipment' OR 
            d.item_type = 'Glassware')"""
    elif id=="Furniture":
        item_type=" d.item_type='Furniture'"
    elif id=="Electronics":
        item_type=" d.item_type='Electronics'"
    elif id=="Computers":
        item_type=" d.item_type='Computer'"
    else:
        item_type=""
    column_names = "d.*, i.issued_qty, i.issued_to, i.issued_date, i.issued_id"
    table_names = "stock_detail d left join stock_issue i"
    where_condition = f"on d.stock_no = i.stock_no where {item_type}"
    result = selectTable(column_names, table_names, where_condition)

    # result = selectTable("d.stock_no,d.item_details,d.date,d.rate,d.total_qty,i.nos_issued,i.balance,i.issued_to,i.issued_date,i.issued_id", "stock_detail d,stock_issue i", f"where d.stock_no=i.stock_no {item_type}")
    return render_template("/home/tables.html",user=current_user,id=id,result=result,timestamp=timestamp)

@views.route('/insert/<id>',methods = ['GET', 'POST'])
def insert(id):
    if request.method=='POST':
        stock_no=request.form['stock_no']
        item_name=request.form['item_name']
        item_type=request.form['item_type']
        rate=request.form['rate']
        date=request.form['date']
        total_qty=request.form['total_qty']
        balance_qty=request.form['balance_qty']
        table_names="stock_detail"
        column_names="(stock_no,item_name,item_type,rate,date,total_qty,balance_qty)"
        values=f"(\'{stock_no}\',\'{item_name}\',\'{item_type}\',{rate},\'{date}\',\'{total_qty}\',\'{balance_qty}\')"
        where_condition=""
        isSuccess=insertTable(table_names,column_names,values,where_condition)
        if isSuccess:
            print("Success insertion on stock_detail")
            flash("Success insertion on stock_detail")
        else:
            print("Unsuccessful insertion on stock_detail")
            flash("Error occured insertion on stock_detail")
        
        issued_qty=request.form['issued_qty']
        issued_to=request.form['issued_to']
        issued_id=request.form['issued_id']
        issued_date=dt.today().strftime('%Y-%m-%d')
        if issued_qty and issued_id and issued_to:
            table_names="stock_issue"
            column_names="(stock_no,issued_qty,issued_to,issued_id,issued_date)"
            values=f"(\'{stock_no}\',\'{issued_qty}\',\'{issued_to}\',\'{issued_id}\',\'{issued_date}\')"
            where_condition=""
            isSuccess=insertTable(table_names,column_names,values,where_condition)
            if isSuccess:
                print("Success insertion on stock_issue")
                flash("Success insertion on stock_issue")
            else:
                print("Unsuccessful insertion on stock_issue")
                flash("Error occured insertion on stock_issue")
    return redirect(url_for('views.stock_details',id=id))

@views.route('/update/<id>/<stockno>/<itemname>',methods=['GET','POST'])
@login_required
def update(id,stockno,itemname):
    if request.method=='POST':
        stock_no=request.form['stock_no']
        item_name=request.form['item_name']
        item_type=request.form['item_type']
        rate=request.form['rate']
        date=request.form['date']
        total_qty=request.form['total_qty']
        balance_qty=request.form['balance_qty']
        table_names="stock_detail"
        column_names=f"""set stock_no=\'{stock_no}\',
                            item_name=\'{item_name}\',
                            item_type=\'{item_type}\',
                            rate=\'{rate}\',
                            date=\'{date}\',
                            total_qty=\'{total_qty}\',
                            balance_qty=\'{balance_qty}\' """
        where_condition=f"where stock_no=\'{stockno}\' and item_name=\'{itemname}\'"
        isSuccess=updateTable(table_names,column_names,where_condition)
        if isSuccess:
            print("Success updation on stock_detail")
            flash("Success updation on stock_detail")
        else:
            print("Unsuccessful updation on stock_detail")
            flash("Error occured updation on stock_detail")

        issued_id=request.form['issued_id']
        issued_qty=request.form['issued_qty']
        issued_to=request.form['issued_to']
        issued_date=dt.today().strftime('%Y-%m-%d')
        if issued_qty and issued_id and issued_to:
            table_names="stock_issue"
            column_names="(stock_no,issued_qty,issued_to,issued_id,issued_date)"
            values=f"(\'{stock_no}\',\'{issued_qty}\',\'{issued_to}\',\'{issued_id}\',\'{issued_date}\')"
            where_condition=f""" on duplicate key update stock_no=\'{stock_no}\',
                                    issued_qty=\'{issued_qty}\',
                                    issued_to=\'{issued_to}\',
                                    issued_id=\'{issued_id}\',
                                    issued_date=\'{issued_date}\'"""
            isSuccess=insertTable(table_names,column_names,values,where_condition)
            if isSuccess:
                print("Success insertion on stock_issue")
                flash("Success insertion on stock_issue")
            else:
                print("Unsuccessful insertion on stock_issue")
                flash("Error occured insertion on stock_issue")
    return redirect(url_for('views.stock_details',id=id))

@views.route('/delete/<id>/<stockno>/<itemname>/<issued_id>',methods=['GET','POST'])
def delete(id,stockno,itemname,issued_id):
    table_names="stock_detail"
    where_condition=f"stock_no=\'{stockno}\' and item_name=\'{itemname}\'"
    isSuccess=deleteTable(table_names,where_condition)
    if isSuccess:
        print("Deleted From stock_detail")
        flash("Deleted From stock_detail")
    else:
        print("Error on deletion From stock_detail")
        flash("Error on deletion From stock_detail")

    if issued_id!='None':
        table_names="stock_issue"
        where_condition=f"issued_id=\'{issued_id}\'"
        isSuccess=deleteTable(table_names,where_condition)
        if isSuccess:
            print("Deleted From stock_issue")
            flash("Deleted From stock_issue")
        else:
            print("Error on deletion From stock_issue")
            flash("Error on deletion From stock_issue")
    return redirect(url_for('views.stock_details',id=id))

@views.route('/test',methods=['GET','POST'])
@login_required
def test():
    
    return render_template("/home/tables.html",user=current_user)