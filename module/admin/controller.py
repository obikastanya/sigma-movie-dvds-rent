from .model import FirstModule

class FirstModuleController():
    def __init__(self):
        self.model=FirstModule()

    def getData(self):
        # get raw data from models, process, then return the responses
        data=self.model.get()

        jsonData={
        'status':True,
        'message':'',
        'data':data
        }
        
        return jsonData

    def getDataModel(self):
        return self.model.getDBData()
