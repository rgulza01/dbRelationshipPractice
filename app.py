from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
import os

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = mysql+pymysql://serveradminloginname:anypassword@servername(containername):3306/anydatabase
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://radiagulzan@db-relationship-practice-mysql:Password123!@db-relationship-practice-mysql.mysql.database.azure.com:3306/examaple_db"
#cnx = mysql.connector.connect(user="radiagulzan@db-relationship-practice-mysql", 
# password={your_password}, 
# host="db-relationship-practice-mysql.mysql.database.azure.com", 
# port=3306, 
# database={your_database}, 
# ssl_ca={ca-cert filename}, 
# ssl_verify_cert=true)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#testing webpage with docker
@app.route('/home')
@app.route('/')
def home():
    return "Bismillah!"


#one owner and many vacuums
class Owner(db.Model):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(255))
    gadgets = db.relationship('Gadget', backref = "owner")
    
    def __repr__(self):
        return f"{self.name} living in {self.address}"

#one owner and many vacuums
class Gadget(db.Model):
    __tablename__ = 'gadget'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100))
    type = db.Column(db.String(100))
    owner_id = db.Column(db.Integer, ForeignKey("owner.id"))

    def __repr__(self):
        return f"model: {self.model}, type: {self.type}"

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)