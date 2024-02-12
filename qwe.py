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

@app.route('/list_prof/<flag>')
def prop(flag):
    proflist = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог',
                   'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                   'штурман', 'пилот дронов']

    return render_template('works.html', flag=flag, proflist=proflist)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
