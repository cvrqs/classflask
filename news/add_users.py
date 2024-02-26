from data.users import User
from data.news import News
from flask import Flask
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/blogs.db")
user = User()
user.name = "Admin"
user.about = "администратор сайта"
user.email = "admin@admin.ru"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()
