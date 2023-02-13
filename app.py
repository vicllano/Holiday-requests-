from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create a Flack instance
app = Flask(__name__)

# Add MYSQL Database 
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://username:password@localhost/requests"

# Initialize the database
db = SQLAlchemy(app)

# Create db Model
class pto_requests(db.Model):
    # Define table columns
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False) 
    end_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    # Create a function to return a string when we add a request
    def __repr__(self):
        return "<Name %r>" % self.id

# Creation of the database tables within the application context.
with app.app_context():
    db.create_all()

# Create route decorators
# Request form page
@app.route("/")
def index():
    return render_template("index.html")

# Submission confirmation page
@app.route("/submitted", methods=["POST"])
def submitted():
    # Create variables from form inputs
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    status = "Pending"
    # Assign variables to database table
    new_request = pto_requests(first_name=first_name, last_name=last_name, email=email, start_date=start_date, end_date=end_date, status=status)

    # If form input values are missing, return error
    if (len(first_name)==0 or len(last_name)==0 or len(email)==0 or len(start_date)==0 or len(end_date)==0):
        error = "All fields required"
        return render_template("index.html", error=error, first_name=first_name, last_name=last_name, email=email, start_date=start_date, end_date=end_date)
    # If start_date is greater than end_date return date_error
    elif start_date > end_date:         
        date_error = "DATE ERROR! Please adjust dates"
        return render_template("index.html", date_error=date_error, first_name=first_name, last_name=last_name, email=email, start_date=start_date, end_date=end_date)
    # else push record to database table and return confirmation
    else:
        try:
            db.session.add(new_request)
            db.session.commit()
            confirmation = "Request Submitted"
            # Return record added to database and pass values into submitted.html
            return render_template("submitted.html", first_name=first_name, last_name=last_name, email=email, start_date=start_date, end_date=end_date, status=status, confirmation=confirmation)
        # If there is a problem adding to the database return other_error and pass it to index.html
        except:
            other_error = "There was an issue! Please try again"
            return render_template("index.html", other_error=other_error, first_name=first_name, last_name=last_name, email=email, start_date=start_date, end_date=end_date)

# Manager's request view page
@app.route("/manager")
def manager():
    # Query all records in database table, order by date_created and store it in all_requests
    all_requests = pto_requests.query.order_by(pto_requests.date_created)
    # Return all records in the database and pass all of it into manager.html as all_requests
    return render_template("manager.html", all_requests=all_requests)

# Update request status page
@app.route("/approvals/<int:id>", methods=["POST", "GET"])
def approvals(id):
    # Query record from database with the id passed from the url and assign to variables
    update = pto_requests.query.get_or_404(id)
    id = update.id
    date_created = update.date_created
    first_name = update.first_name
    last_name = update.last_name
    email = update.email
    start_date = update.start_date
    end_date = update.end_date
    # If submit button clicked, update status to new value from the form dropdown
    if request.method == "POST":
        update.status = request.form["status"]
        # Push updated record to database table
        try:
            db.session.commit()
            update_confirmation = "Update Successful"
            # Query all records in database table, order by date_created and store it in all_requests
            all_requests = pto_requests.query.order_by(pto_requests.date_created)
            # Return all records in the database and pass all of it into manager.html as all_requests
            return render_template("manager.html", update_confirmation=update_confirmation, all_requests=all_requests)
        # If there is a problem updating the database return message
        except:
            return "ERROR! there was a problem"
    else:
        return render_template("approvals.html", update=update, first_name=first_name, last_name=last_name, email=email, start_date=start_date, end_date=end_date)

# Employee's request view page
@app.route("/request_status")
def request_status():
    # Query all records in database table, order by date_created and store it in request_status
    request_status = pto_requests.query.order_by(pto_requests.date_created)
    return render_template("request_status.html", request_status=request_status)

# Execute script
if __name__ == "__main__":
    app.run(debug=True)
