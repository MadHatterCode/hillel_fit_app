from flask import Flask, request
import db_utils
import forms

app = Flask(__name__)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        form_data = request.form
        db_utils.insert_into_db(f"INSERT INTO user(login, password, birth_date, phone) VALUES (\"{form_data['login']}\", \"{form_data['password']}\", \"{form_data['birth_date']}\", "
                                f"\"{form_data['phone']}\")")
        return 'user registered'
    elif request.method == "GET":
        return forms.registration_form()
    else:
        return "Invalid request method"


@app.route("/user", methods=["GET", "PUT", "POST"])
def user():
    if request.method == "GET":
        return db_utils.get_from_db('SELECT * FROM user WHERE id=1')
    else:
        return "Invalid request method"


@app.route("/user/funds", methods=["GET", "POST"])
def user_funds():
    if request.method == "GET":
        return db_utils.get_from_db('SELECT funds FROM user WHERE id=1')
    elif request.method == "POST":
        return "Adding or removing funds from user's account"
    else:
        return "Invalid request method"


@app.route("/user/reservations", methods=["GET", "POST"])
def user_reservations():
    if request.method == "GET":
        return db_utils.get_from_db("SELECT * FROM reservation WHERE user_id=1", multiple=True)
    elif request.method == "POST":
        return "Making a new reservation"
    else:
        return "Invalid request method"


@app.route("/user/reservations/<int:reservation_id>", methods=["GET", "PUT", "DELETE"])
def user_reservation_details(reservation_id):
    if request.method == "GET":
        return db_utils.get_from_db("SELECT * FROM reservation WHERE reservation_id=reservation_id AND user_id=1", multiple=True)
    elif request.method == "PUT":
        return f"Updating reservation ID {reservation_id}"
    elif request.method == "DELETE":
        return f"Cancelling reservation ID {reservation_id}"
    else:
        return "Invalid request method"


@app.route("/user/checkout", methods=["GET", "POST", "PUT"])
def user_checkout():
    if request.method == "GET":
        return "checkout information"
    elif request.method == "POST":
        return "Submitting checkout request"
    elif request.method == "PUT":
        return "Updating checkout details"
    else:
        return "Invalid request method"


@app.route("/fitness_center", methods=["GET"])
def fitness_center():
    return db_utils.get_from_db("SELECT name, address FROM fitness_center", multiple=True)


@app.route("/fitness_center/<int:fitness_center_id>", methods=["GET"])
def fitness_center_details(fitness_center_id):
    return db_utils.get_from_db(f"SELECT name, address FROM fitness_center WHERE id={fitness_center_id}")


@app.route("/fitness_center/<int:fitness_center_id>/trainer", methods=["GET"])
def fitness_center_trainers(fitness_center_id):
    return db_utils.get_from_db(f"SELECT name FROM trainer WHERE fitness_center_id={fitness_center_id}", multiple=True)


@app.route("/fitness_center/<int:fitness_center_id>/trainer/<int:trainer_id>", methods=["GET"])
def fitness_center_trainer_details(fitness_center_id, trainer_id):
    return db_utils.get_from_db(f"SELECT name FROM trainer WHERE fitness_center_id={fitness_center_id} AND id={trainer_id}")


@app.route("/fitness_center/<int:fitness_center_id>/trainer/<int:trainer_id>/rating", methods=["GET", "POST", "PUT"])
def fitness_center_trainer_rating(fitness_center_id, trainer_id):
    if request.method == "GET":
        return db_utils.get_from_db(f"SELECT ROUND(AVG(points),0) as rating FROM review WHERE fitness_center_id={fitness_center_id} AND trainer_id={trainer_id}", multiple=True)
    elif request.method == "POST":
        return f"Submitting a new rating for trainer ID {trainer_id} at fitness center ID {id}"
    elif request.method == "PUT":
        return f"Updating existing rating for trainer ID {trainer_id} at fitness center"



