from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route('/<title>')
@app.route('/index/<title>')
def prepare(title):
    user = "Ученик Яндекс.Лицея"
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)
print("1")

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
