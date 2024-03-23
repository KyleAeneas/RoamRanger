from . import api_bp
from flask import  jsonify, request
import datetime
from app.extensions import mongo
from flask import current_app

@api_bp.post('/Patrol_Data')
def add_sensor_reads():
    Patrol_Data = request.get_json()

    RFID = Patrol_Data['RFID']
    Area_ID = Patrol_Data['Area_ID']
    
    current_app.logger.info(f"Patrol_Data : {Patrol_Data}")
    
    Patrol_Data = {"timestamp": datetime.datetime.now(), "metadata": {"Area_ID": Area_ID}, "RFID": RFID,}
    
    mongo.db.Patrol_Data.insert_one(Patrol_Data)
    
    return jsonify({"Status": "OK", "Message": "Successfully saved sensor records!"})
