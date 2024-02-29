from data.users import User
from flask import Flask
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/blogs.db")
job = Jobs()
job.team_leader = 3
job.job = 'Посадить деревья'
job.work_size = 10
job.collaborators = '1, 2, 3'
job.is_finished = False
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()
