# services/users/project/api/users/views.py


from flask import Blueprint, jsonify, request


from flask_cors import CORS, cross_origin
from datetime import datetime 

from flask_restx import Resource, fields, Namespace

from math import sin, cos, sqrt, atan2, radians


from .models import Location
from project import create_app, db



import json 


from project.api.users.crud import (
    get_all_users,
    get_user_by_email,
    add_user,
    get_user_by_id,
    update_user,
    delete_user,
)

main = Blueprint('main', __name__)



cors = CORS(main, resources={r"/coords": {"origins": "*"}})

cors2 = CORS(main, resources={r"/movies": {"origins": "*"}})



users_namespace = Namespace("users")

user = users_namespace.model(
    "User",
    {
        "id": fields.Integer(readOnly=True),
        "username": fields.String(required=True),
        "email": fields.String(required=True),
        "created_date": fields.DateTime,
    },
)

user_post = users_namespace.inherit(
    "User post", user, {"password": fields.String(required=True)}
)


class UsersList(Resource):
    @users_namespace.marshal_with(user, as_list=True)
    def get(self):
        """Returns all users."""
        return get_all_users(), 200

    @users_namespace.expect(user_post, validate=True)
    @users_namespace.response(201, "<user_email> was added!")
    @users_namespace.response(400, "Sorry. That email already exists.")
    def post(self):
        """Creates a new user."""
        post_data = request.get_json()
        username = post_data.get("username")
        email = post_data.get("email")
        password = post_data.get("password")
        response_object = {}

        user = get_user_by_email(email)
        if user:
            response_object["message"] = "Sorry. That email already exists."
            return response_object, 400
        add_user(username, email, password)
        response_object["message"] = f"{email} was added!"
        return response_object, 201


class Users(Resource):
    @users_namespace.marshal_with(user)
    @users_namespace.response(200, "Success")
    @users_namespace.response(404, "User <user_id> does not exist")
    def get(self, user_id):
        """Returns a single user."""
        user = get_user_by_id(user_id)
        if not user:
            users_namespace.abort(404, f"User {user_id} does not exist")
        return user, 200

    @users_namespace.expect(user, validate=True)
    @users_namespace.response(200, "<user_is> was updated!")
    @users_namespace.response(404, "User <user_id> does not exist")
    def put(self, user_id):
        """Updates a user."""
        post_data = request.get_json()
        username = post_data.get("username")
        email = post_data.get("email")
        response_object = {}

        user = get_user_by_id(user_id)
        if not user:
            users_namespace.abort(404, f"User {user_id} does not exist")
        update_user(user, username, email)
        response_object["message"] = f"{user.id} was updated!"
        return response_object, 200

    @users_namespace.response(200, "<user_is> was removed!")
    @users_namespace.response(404, "User <user_id> does not exist")
    def delete(self, user_id):
        """Updates a user."""
        response_object = {}
        user = get_user_by_id(user_id)
        if not user:
            users_namespace.abort(404, f"User {user_id} does not exist")
        delete_user(user)
        response_object["message"] = f"{user.email} was removed!"
        return response_object, 200


users_namespace.add_resource(UsersList, "")
users_namespace.add_resource(Users, "/<int:user_id>")


@main.route('/test')
def test(): 
    
    return 'Test method worked', 201


cors = CORS(main, resources={r"/coords": {"origins": "*"}})
@main.route('/coords')
def coords():
    
    
    coords = []
 
    f = open('data.json',)

    data = json.load(f) 
     

    for key, valu in data.items(): 
        print(key, valu)
        
    f.close() 

    coords.append(data)

 

    return jsonify({"coords": coords})



@main.route('/incomingCoords', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def incomingCoords(): 


    
    coords2 = request.get_json()     
    #movies = []
    coords2Str = str(coords2)
    
    #text_file = open("sample.txt", "w")
    #n = text_file.write(coords2Str)
    #text_file.close()
    new_location = Location(lat=coords2['lat'], lng=coords2['lng'])

    db.session.add(new_location)
    db.session.commit()


    with open('data.json', 'w') as f:
        json.dump(coords2, f)

    #with open('sample.txt', 'r') as myfile:
    #    data = myfile.read()
    #print(data)


    return 'Done', 201





cors3 = CORS(main, resources={r"/locationreport": {"origins": "*"}})
@main.route('/locationreport')
def locationreport(): 
    '''
    location_list = Location.query.all()

    locations = []



    for location in location_list:
        locations.append({'lat' : location.lat, 'lng' : location.lng, 'time' : location.time})
    
    return jsonify(locations)
    '''

    waypoints_list = Location.query.all()

    waypoints = []


    #Getting todays date waypoints 
     
    for waypoint in waypoints_list:
        timeStr = str(waypoint.time)
        time = datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S.%f')
        
        if time.date() == datetime.today().date(): 
            waypoints.append({'lat' : waypoint.lat, 'lng' : waypoint.lng, 'time' : waypoint.time})
    

   


    startends = [0]
    waypointsLen = len(waypoints)

    for x in range(0, waypointsLen - 1): 
        timestr1 = str(waypoints[x]['time'])
        timestr2 = str(waypoints[x + 1]['time'])
       
        time1 =  datetime.strptime(timestr1, '%Y-%m-%d %H:%M:%S.%f') 
        time2 =  datetime.strptime(timestr2, '%Y-%m-%d %H:%M:%S.%f') 
        diffinsecs =  time2 - time1
        if diffinsecs.seconds > 90: 
            startends.append(x)
        print('diff in secs')
        print(diffinsecs.seconds)
        print('')

    print('startends')
    print(startends)
    locationsFinal = []
    locationsFinal.append(waypoints[startends[0]])



    for x in range(0, len(startends)):
        print(x)
        if x % 2  != 0: 
            locationsFinal.append(waypoints[startends[x]])
            
            print("Moving waypoints to locationsFinal")
            print(startends[x])
            print('')

    print("locationsFinal")
    print(locationsFinal)

    
 

    return jsonify(locationsFinal)






cors4 = CORS(main, resources={r"/tripsreport": {"origins": "*"}})
@main.route('/tripsreport')
def tripsreport(): 
    
    waypoints_list = Location.query.all()

    waypoints = []


    #Getting todays date waypoints 
     
    for waypoint in waypoints_list:
        timeStr = str(waypoint.time)
        time = datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S.%f')
        
        if time.date() == datetime.today().date(): 
            waypoints.append({'lat' : waypoint.lat, 'lng' : waypoint.lng, 'time' : waypoint.time})
    

   


    startends = [0]
    waypointsLen = len(waypoints)

    for x in range(0, waypointsLen - 1): 
        timestr1 = str(waypoints[x]['time'])
        timestr2 = str(waypoints[x + 1]['time'])
       
        time1 =  datetime.strptime(timestr1, '%Y-%m-%d %H:%M:%S.%f') 
        time2 =  datetime.strptime(timestr2, '%Y-%m-%d %H:%M:%S.%f') 
        diffinsecs =  time2 - time1
        if diffinsecs.seconds > 90: 
            startends.append(x)
        print('diff in secs')
        print(diffinsecs.seconds)
        print('')

    print('startends')
    print(startends)



    

    tripsAllWaypoints = []
    for x in range(0, len(startends) - 1):
        start = startends[x] 
        end = startends[x+1]
        tripsAllWaypoints.append(waypoints[start : end])
    
    print('Trips')
    print(tripsAllWaypoints)






    
    tripsAllWaypoints2 = []
    for trip in tripsAllWaypoints: 
        print('Trips devided')
        print (trip)
        tripLen = len(trip)
        intervals = []
        #tripsAllWaypoints2.append([trip, {'topSpeeed' : 100 }])
        
           #Intervals pushed to array 
        for x in range(0, tripLen - 1): 
            print("Trip dev waypoint")
            print(trip[x])
            interval = {'int1' : trip[x], 'int2' : trip[x + 1]}
            print('Interval')
            print(interval)
        
            intervals.append(interval)
        
        print('Intervals: ')
        print(intervals)

        
        intervalDistTimes = []
        #calc interval speeds 
        for intrs in intervals: 
            print('Interval:')
            print(intrs['int1']['lat'])
            print(intrs['int2']['lat'])
            R = 6373.0

            lat1 = radians(intrs['int1']['lat'])
            lon1 = radians(intrs['int1']['lng'])
            lat2 = radians(intrs['int2']['lat'])
            lon2 = radians(intrs['int2']['lng'])

            dlon = lon2 - lon1
            dlat = lat2 - lat1

            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))

            distance = R * c

            print("Result:", distance)
            


            time1 = intrs['int1']['time']
            time2 = intrs['int2']['time']
            
        
            #interval 
            print (time1)
            print (time2)
            time_delta = (time2 - time1) 
            time = time_delta.total_seconds()
            print(time)


            speed = distance / (time / 3600)
            print('kph')
            print(speed)


            
            intervalDistTimes.append(speed)

        
        maxSpeed = max(intervalDistTimes)
        print('Interval Dist times')
        print(intervalDistTimes)
        print('Max value')
        print(maxSpeed)
        tripsAllWaypoints2.append([{"waypoints" : trip}, {'topSpeed' : maxSpeed }])
        
    tripsStartEnds = []
    for startend in tripsAllWaypoints2: 
        print('Start')
        print(startend)
        print('topSpeed')
        print(startend[1]['topSpeed'])
        topSpeed =startend[1]['topSpeed'] 
        start = startend[0]['waypoints'][0]
        end = startend[0]['waypoints'][len(startend) - 1]
        tripsStartEnds.append({'trip' : {'start' : start, 'end' : end}, 'topSpeed' : topSpeed })
  

    return jsonify(tripsStartEnds)