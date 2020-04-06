import pymongo
from pymongo import MongoClient
from pymongo import errors
import datetime



#obj_log = ApiLogs()
 

class Model():

    obj_db     = ""
    obj_client = ""

    def __init__(self, obj_logs):
        self.obj_logs =  obj_logs

    def getConnection(self, host, dbName):
        try:
            
            client = MongoClient(host)
           
            db     = client.get_database(dbName)
        except Exception as e:

            self.obj_logs.menthod_log_error(
                error = {
                    "error_type":"stop",
                    "errroe_msg":"Something went wrong while connecting dataserver",
                    "error_desc":" " + str(e) + ""
                })
           

        else:

            self.obj_logs.method_reurned_parameter(
                conn = db,
                client = client          
            )

            self.obj_db     = db
            self.obj_client = client

            #return obj_log

    def closeConnection(self, client=None):

        try:
           if client == None:
                client = self.obj_client
           client.close()

        except Exception as e:
            self.obj_logs.menthod_log_error(
                error = {
                    "error_type":"warning",
                    "errroe_msg":"Something went wrong while connecting dataserver",
                    "error_desc":str(e)
                })
            
            #return obj_log

        else:
            self.obj_logs.method_reurned_parameter(
                obj_con_close=True         
            )
            #return obj_log

    def insertOneRecord(self,collection_name , docObj,db=None):

        try:
            if  db == None:
                db = self.obj_db
         
            users = db[collection_name]
            result = users.insert_one(docObj)

        except Exception as e:
            self.obj_logs.menthod_log_error(
                error = {
                    "error_type":"stop",
                    "errroe_msg":"Something went wrong while inserting record",
                    "error_desc":str(e)
                })
            #return obj_log
        else:
            self.obj_logs.method_log_success(
                success = {
                    "Msg":"Record inserted successfully",
                    "desc":str(result)
                })
            #return obj_log

    def FindOne(self,collection_name , query , proj={"_id":0}, check=False,db=None):
        
        try:
            if db == None:
                db = self.obj_db
            
            
            users = db[collection_name]
            
            result = users.find_one(query,proj)
           
            
            if result != None and check==True:
                self.obj_logs.menthod_log_error(
                error = {
                    "error_type":"stop",
                    "msg":"Record already exists with this user, cannot insert"
                })
                #return obj_log

        except Exception as e:
            
            self.obj_logs.menthod_log_error(
            error = {
                    "error_type":"stop",
                    "msg":"Sommething went wrong while getting record",
                    "desc":str(e)
                })
            #return obj_log
        else:
            self.obj_logs.method_log_success(
                success = {
                    collection_name:result
                })
            #return obj_log

    def updateOne(self,collection_name,filter,update,upsert=False,bypass_document_validation=False, collation=None, array_filters=None, session=None,db=None):
        
        try:
            if db == None:
                db = self.obj_db

            users = db[collection_name]
            
            result = users.update_one(filter,update,upsert)
            
        except Exception as e:
            self.obj_logs.menthod_log_error(
            error = {
                    "error_type":"stop",
                    "msg":"Sommething went wrong while updating record",
                    "desc":str(e)
                })
        else:
            self.obj_logs.method_log_success(
                success = {
                    collection_name:result
                })



            
        
