from flask import app, render_template, request, redirect
from app.models import Divvy
from app import app


@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html')


@app.route('/calculate')
def calculate():
    keys = request.args.to_dict().keys()
    if 'start' in keys and 'end' in keys:
        from_station_id = request.args.to_dict().get('from_station_id', None)
        start = request.args.to_dict()['start']
        end = request.args.to_dict()['end']
        divvy = Divvy.query.filter(Divvy.starttime.between(start, end)).all()
        total_duration = 0
        for i in range(len(divvy)):
            total_duration = total_duration + divvy[i].trip_duration
        average_duration = total_duration/len(divvy) 
        return {"average_duration": average_duration}
