from Appserver import custom_func

def func_insert_user(obj_model,obj_doc):
   try:

               #checking whether record exist with the same userId in USERS table
        myQuery = {
            "user_id":obj_doc["user_id"]
        }
        
        #checking whether record exist or not
        obj_model.FindOne("USERS", myQuery, proj={"_id":1}, check=True)
        
        if obj_model.obj_logs.var_error == True:
            return 0

        #Verifying OTP
        myQuery = {
            "user_id":obj_doc["user_id"],
            "user_ip":obj_doc["user_ip"],
            "otp"    :obj_doc["otp"] 
        }

        
        obj_model.FindOne("OTPS", myQuery, proj={"otp":1, "last_modified":1})

        if obj_model.obj_logs.var_error == True:
            return 0
        
        if obj_model.obj_logs.obj_returned["OTPS"] == None:
            obj_model.obj_logs.menthod_log_error(
                error = {
                        "error_type":"stop",
                        "msg":"Invalid Otp"
                    })
            return 0

        last_modified = (obj_model.obj_logs.obj_returned["OTPS"])["last_modified"]
        
        #return if otp expired
        timeDiff = custom_func.func_get_time_diff(last_modified)

        if timeDiff["minutes"] > 10:

            
            obj_model.obj_logs.menthod_log_error(
                error = {
                        "error_type":"stop",
                        "msg":"Otp expired"
                    })
            return 0


        
        recordToInsert={
            "user_id"   :obj_doc["user_id"],
            "user_ips"  :[obj_doc["user_ip"]],
            "user_pass" :obj_doc["user_pass"],
            "last-login": str(custom_func.datetime.datetime.now())
        }

        obj_model.insertOneRecord("USERS", recordToInsert)
        
        if obj_model.obj_logs.var_error == True:
            return 0

       
        jwtToken = custom_func.func_create_custom_token(
                {
                    "user_id"   : obj_doc["user_id"],
                    "user_pass" : obj_doc["user_pass"]
                    }
            )
       
        obj_model.obj_logs.method_log_success(token = jwtToken)
        return 0

   except Exception as e:
        obj_model.obj_logs.menthod_log_error(
                error = {
                        "error_type":"stop",
                        "msg":"Something went wrong",
                        "desc":str(e)
                    })
        return 0



def func_get_user_info(obj_model,obj_doc):



    myQuery = {    "$and":
            [
                {
                    "user_id":obj_doc["user_id"] 
                },
                {
                    "user_pass":obj_doc["user_pass"]
                }
            ]
        }
    
    obj_model.FindOne("USERS", myQuery)
    if obj_model.obj_logs.obj_returned["USERS"] == None:
            obj_model.obj_logs.menthod_log_error(
                error = {
                        "error_type":"stop",
                        "desc":"Invalid login credintial"
                    })
            return 0

    #checking error in api log
    if obj_model.obj_logs.var_error == True:
        return 0



    