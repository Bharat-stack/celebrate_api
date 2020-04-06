import importlib
import sys

from Appserver.model import Model

class RunApi:
    
    def  __init__(self, obj_logs):
        self.obj_logs = obj_logs

    def method_process_req(self,reqJsonObj):
        obj_logs = self.obj_logs

        for key in reqJsonObj:
            if key == "action":
                action = reqJsonObj[key]
            if key == "db":
                db=reqJsonObj[key]
            if key=="method":
                method = reqJsonObj[key]
            if key=="obj_doc":
                objDoc=reqJsonObj[key]
                
            if key=="host":
                host=reqJsonObj[key]
        


        #validate will work later on this
        obj_model = Model(obj_logs)
        #print("Appserver") 
        obj_model.getConnection(host,db)
        
        if obj_logs.var_error == True:
            return 0

        #Creating connection object, saving these values in logs

        try:
            #getting the class name i.e Appserver API to be called and its method from db processing
            ClassName=  importlib.import_module(method)
            func = getattr(ClassName, action)
            
            #calling Appserver API action and giving required parameter
            func(obj_model,objDoc)


            obj_model.closeConnection()
        
        except Exception as e:
            
            obj_model.closeConnection()
            
            obj_logs.menthod_log_error(
                error = {
                    "error_type":"fatal",
                    "error_msg" :"something went wrong",
                    "desc"      : str(e)
                }
            )
  








