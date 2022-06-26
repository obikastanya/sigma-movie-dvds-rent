class Resp:
    @staticmethod  
    def make( message='', status=False, data=[]) -> dict:
        """For select result"""
        return {'status':status, 'message':message, 'data':data}

    @staticmethod  
    def withoutData( message='', status=False) -> dict:
        """For execution result (insert, update,delete)"""
        return {'status':status, 'message':message}

        
    @staticmethod
    def makeLov(data)-> dict:
        """For lov with key value pair"""
        lov=[]
        for item in data:
            lov.append({'id':item[0],'value':item[1]})
        return lov
    

    @staticmethod
    def map(keys,values)-> dict:
        """Map list of key with list of values. Sample keys=['id','desc'] values=[[1,''],[2,'']] """
        data=[]
        for value in values:
            record={}
            for index, key in enumerate(keys):
                record[key]=value[index]
            data.append(record)
        return data

    @staticmethod
    def datatable(status=True, msg='',data={}):
        response={'status':status, 'msg':msg, 'data':data.get('datas'), 'recordsTotal':data.get('totalRecords')}
        if data.get('totalRecordsFiltered') !=None:
            response.update({'recordsFiltered':data.get('totalRecordsFiltered')})
        else:
            response.update({'recordsFiltered':data.get('totalRecords')})
        return response
