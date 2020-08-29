from project import app
from flask import render_template

# froms
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route('/')
def index():
    data = {
        "risk": 2,
        "no_risk": 1
    }
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run()