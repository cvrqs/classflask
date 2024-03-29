from flask import Flask, url_for, render_template, redirect
from data.users import User
from flask import Flask
from data.login_form import LoginForm
from flask_login import LoginManager, login_manager, login_user, login_required
from data import db_session
from data.jobs import Jobs
from data.works_form import WorksForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

db_session.global_init('db/mars_explorer.db')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
@app.route('/index')
def index():
    db_sess = db_session.create_session()

    jobs = db_sess.query(Jobs).all()

    return render_template('jobs.html', jobs=jobs)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/add_jobs', methods=['GET', 'POST'])
@login_required
def add_jobs():
    form = WorksForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs()
        job.team_leader = form.team_leader.data
        job.job = form.job.data
        job.work_size = form.work_size.data
        job.collaboratos = form.collaboratos.data
        job.is_finished = form.is_finished.data

        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('add_jobs.html', title='Добавление работы',
                           form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
