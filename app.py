from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/heroes/')
def hero():
    return render_template('hero.html')



@app.route('/heroes/<name>/')
def heroes(name):
    if name == 'Warrior' or name == 'Archer' or name == 'Mag':
        return render_template('For_Heroe.html', name=name)

    else:
        return render_template('War.html')


if __name__ == '__main__':
    app.run()
