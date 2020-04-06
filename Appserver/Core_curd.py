import pymongo
from pymongo import MongoClient
import datetime

from api_log import ApiLogs

obj_api_logs = ApiLogs()


class CreateRecord:

    def insertOneRecord(self, db, collection_name , docObj):

        try:
            users = db[collection_name]
            result = users.insert_one(docObj)

        except Exception as e:
            obj_api_logs.menthod_log_error(
                error = {
                    "error_type":"stop",
                    "errroe_msg":"Something went wrong while adding record",
                    "error_desc":str(e)
                })
            return obj_api_logs
        else:
            obj_api_logs.method_log_success(
                success = {
                    "Msg":"Record inserted successfully",
                    "desc":str(result)
                })
            return obj_api_logs

class FindRecord:

    def FindOne(self,db, collection_name , query , check=False, proj={"_id":0}):

        try:
            users = db[collection_name]
            print(query)
            print(proj)
            result = users.find_one(query,proj)
           
            if result != None and check:
                obj_api_logs.menthod_log_error(
                error = {
                    "error_type":"stop",
                    "msg":"Record already exists with this user, cannot insert"
                })
                return obj_api_logs

        except Exception as e:
            obj_api_logs.menthod_log_error(
            error = {
                    "error_type":"stop",
                    "msg":"Sommething went wrong while getting record",
                    "desc":str(e)
                })
            return obj_api_logs
        else:
            obj_api_logs.method_log_success(
                success = {
                    collection_name:result
                })
            return obj_api_logs
    