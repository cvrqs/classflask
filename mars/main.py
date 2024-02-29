from flask import Flask, url_for, render_template
from data.users import User
from flask import Flask
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


    db_session.global_init('db/blogs.db')

    db_sess = db_session.create_session()

    jobs = db_sess.query(Jobs).all()


    return render_template('jobs.html', jobs=jobs)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
