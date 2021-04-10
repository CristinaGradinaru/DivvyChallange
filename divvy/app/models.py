from app import db
from datetime import datetime

class Divvy(db.Model):
    trip_id= db.Column(db.Integer, primary_key = True)
    starttime= db.Column(db.DateTime, nullable= False)
    stoptime= db.Column(db.DateTime, nullable= False)
    bikeid= db.Column(db.Integer, nullable=False)
    from_station_id = db.Column(db.Integer)
    from_station_name = db.Column(db.String)
    to_station_id = db.Column(db.Integer)
    to_station_name = db.Column(db.String)
    usertype = db.Column(db.String)
    gender = db.Column(db.String)
    birthday = db.Column(db.String)
    trip_duration = db.Column(db.Integer)

    def __init__(self):
        self.trip_id= trip_id
        self.starttime= starttime
        self.stoptime = stoptime
        self.bikeid = bikeid
        self.from_station_id= from_station_id
        self.from_station_name= from_station_name
        self.to_station_id = to_station_id
        self.to_station_name = to_station_name
        self.usertype = usertype
        self.gender = gender
        self.birthday=birthday
        self.trip_duration = trip_duration


