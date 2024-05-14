from flask import Flask, request

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Credentials accepted, logging in"
    elif request.method == "GET":
        return "Retrieving information about the user to render login form"
    else:
        return "Invalid request method"


@app.route("/user", methods=["GET", "PUT", "POST"])
def user():
    if request.method == "GET":
        return "Retrieving user information"
    elif request.method == "PUT":
        return "Updating user information"
    elif request.method == "POST":
        return "Creating a new user"
    else:
        return "Invalid request method"


@app.route("/user/funds", methods=["GET", "POST"])
def user_funds():
    if request.method == "GET":
        return "Retrieving user's funds information"
    elif request.method == "POST":
        return "Adding or removing funds from user's account"
    else:
        return "Invalid request method"


@app.route("/user/reservations", methods=["GET", "POST"])
def user_reservations():
    if request.method == "GET":
        return "Retrieving user's reservations"
    elif request.method == "POST":
        return "Making a new reservation"
    else:
        return "Invalid request method"


@app.route("/user/reservations/<int:reservation_id>", methods=["GET", "PUT", "DELETE"])
def user_reservation_details(reservation_id):
    if request.method == "GET":
        return f"Retrieving details for reservation ID {reservation_id}"
    elif request.method == "PUT":
        return f"Updating reservation ID {reservation_id}"
    elif request.method == "DELETE":
        return f"Cancelling reservation ID {reservation_id}"
    else:
        return "Invalid request method"


@app.route("/user/checkout", methods=["GET", "POST", "PUT"])
def user_checkout():
    if request.method == "GET":
        return "Preparing checkout information"
    elif request.method == "POST":
        return "Submitting checkout request"
    elif request.method == "PUT":
        return "Updating checkout details"
    else:
        return "Invalid request method"


@app.route("/fitness_center", methods=["GET"])
def fitness_center():
    return "Retrieving general information about the fitness center"


@app.route("/fitness_center/<int:id>", methods=["GET"])
def fitness_center_details(id):
    return f"Retrieving details for fitness center ID {id}"


@app.route("/fitness_center/<int:id>/trainer", methods=["GET"])
def fitness_center_trainers(id):
    return f"Retrieving list of trainers for fitness center ID {id}"


@app.route("/fitness_center/<int:id>/trainer/<int:trainer_id>", methods=["GET"])
def fitness_center_trainer_details(id, trainer_id):
    return f"Retrieving details for trainer ID {trainer_id} at fitness center ID {id}"


@app.route("/fitness_center/<int:id>/trainer/<int:trainer_id>/rating", methods=["GET", "POST", "PUT"])
def fitness_center_trainer_rating(id, trainer_id):
    if request.method == "GET":
        return f"Retrieving rating for trainer ID {trainer_id} at fitness center ID {id}"
    elif request.method == "POST":
        return f"Submitting a new rating for trainer ID {trainer_id} at fitness center ID {id}"
    elif request.method == "PUT":
        return f"Updating existing rating for trainer ID {trainer_id} at fitness center
