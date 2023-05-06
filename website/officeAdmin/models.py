from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



#Users table in master_db
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    usertype = db.Column(db.String(150))
    department = db.Column(db.String(150))


# ______________________________stock_details table
# create table stock_detail (
# date date,
# item_details varchar(100),
# rate numeric(7,3),
# total_qty varchar(50),
# stock_no varchar(50)
# );
# ALTER TABLE stock_detail
# ADD COLUMN item_type varchar(50);



# _______________________________stock_issue table
# create table stock_issue(
# stock_no varchar(50),
# nos_issued varchar(50),
# balance varchar(50),
# issued_to varchar(50),
# issued_id varchar(50)
# );
# alter table stock_issue add column issue_date date after issued_to;

# _______________________________view that joins both stock_detail and stock_issue
# CREATE VIEW stock_details_view AS
# SELECT
#     sd.date,
#     sd.item_details,
#     sd.rate,
#     sd.total_qty,
#     si.nos_issued,
#     si.balance,
#     si.issued_to,
#     si.issued_id
# FROM stock_detail sd
# LEFT JOIN stock_issue si ON sd.stock_no = si.stock_no;

# SELECT * FROM stock_details_view;
