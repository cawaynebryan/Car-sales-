# https://www.carsales.com.au/
# https://mdbootstrap.com/docs/standard/extended/gallery/
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 's0x8;\#%#/5?$34444443'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    price = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    body_type = db.Column(db.String(100), nullable=False)
    transmission = db.Column(db.String(100), nullable=False)
    fuel_type = db.Column(db.String(100), nullable=False)
    drivetrain = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(5000), nullable=False)
    mileage = db.Column(db.Integer)
    imported = db.Column(db.String(5000), nullable=False)
    Color = db.Column(db.String(100), nullable=False)
    doors = db.Column(db.Integer)


#db.create_all()


new_car = Car(
    make='Toyota',
    status='Used',
    model='2012',
    body_type='SUV',
    transmission='manual',
    fuel_type='Gas',
    drivetrain='4WD',
    year='2012',
    mileage='390',
    Color='Red',
    doors='4',
    comment='Mints Condition, Price negotiable',
    imported='Local owned',
    name='Toyota Rav 4',
    price='1.8M'
)

# db.session.add(new_car)
# print(new_car)
# db.session.commit()



#all_cars = db.session.query(Car.make).distinct().all()


def dictionary(make):
    all_cars = Car.query.filter_by(make=make).all()
    for new_make in all_cars:
        print(new_make.make)

dictionary("Nisan")



@app.route("/")
def home_view():
    return render_template('home_page.html')


@app.route("/inventory")
def inventory_view():
    all_cars = Car.query.all()
    return render_template("inventory_page.html", cars=all_cars)


@app.route("/about")
def about_view():
    return render_template("about_page.html")


@app.route("/detail")
def detail_view():
    return render_template("detail_page.html")


@app.route("/admin")
def admin_view():
    return render_template("admin_page.html")


if __name__ == "__main__":
    app.run(debug=True)
