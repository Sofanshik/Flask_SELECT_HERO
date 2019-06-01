from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/heroes/<name>/')
def hero(name):
    if name == 'Warrior' or name == 'Archer' or name == 'Mag':
        return render_template('Mag.html')

    else:
        return render_template('War.html')


if __name__ == '__main__':
    app.run()
