import pymongo
from pymongo import MongoClient
from pymongo import errors
from api_log import ApiLogs

obj_api_logs = ApiLogs()


class Connection:

    def getConnection(self, host , port , dbName):
        try:
            client = MongoClient(host, port)
            db     = client[dbName]
        except Exception as e:

            obj_api_logs.menthod_log_error(
                error = {
                    "error_type":"Fatal",
                    "errroe_msg":"Something went wrong while connecting dataserver",
                    "error_desc":str(e)
                })
            
            return obj_api_logs

        else:

            obj_api_logs.method_reurned_parameter(
                conn = db,
                client = client          
            )

            return obj_api_logs

    def closeConnection(self, client):

        try:
           
           client.close()

        except Exception as e:
            obj_api_logs.menthod_log_error(
                error = {
                    "error_type":"Fatal",
                    "errroe_msg":"Something went wrong while connecting dataserver",
                    "error_desc":str(e)
                })
            
            return obj_api_logs

        else:
            obj_api_logs.method_reurned_parameter(
                obj_con_close=True         
            )
            return obj_api_logs


    