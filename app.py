from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdbname.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class User_info(db.Model):
    email = db.Column(db.String(50), primary_key = True)
    password = db.Column(db.String(50), nullable = False)

    def __repr__(self)->str:
        return f"{self.email} - {self.password}"


@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()   
    app.run(debug=True)



