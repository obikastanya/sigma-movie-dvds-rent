import os
from flask import request
from werkzeug.utils import secure_filename
from lib.response import Resp
from app import db
from orm.alert import Alert, AlertSchema
from orm.user import User, UserSchema


class AlertController:

    def getAlerts():
        id=request.json.get('userId')
        print(id)
        user=User.query.filter_by(msu_id=id).first()
        userJson=UserSchema().dump(user)
        alerts=Alert.query.filter(Alert.al_read_status=='N', Alert.al_msu_id==id ).all()
        # AlertController.updateAlertStatus(alerts)
        jsonAlertsData=AlertSchema(many=True).dump(alerts)
        userJson.update({'alerts': jsonAlertsData})
        resp=Resp.make(data=[userJson],status=True)
        return resp
    
    def updateAlertStatus(alerts):
        for alert in alerts:
            alert.al_read_status='Y'
            db.session.commit()
    
