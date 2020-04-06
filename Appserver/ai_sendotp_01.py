from Appserver import SendEmail,send_sms



import datetime
from datetime import timedelta


def func_SendOtp(obj_model,obj_doc):
    
    # if len(obj_doc) != 2 or not("user_ip" in obj_doc)  or (not(""):
    #     obj_model.obj_logs.menthod_log_error(
    #                 error = {
    #                     "error_type":"stop",
    #                     "errroe_msg":"Invalid req body"
    #                  }
    #             )

       
    '''
        Purpose: validate and sends otps, handle both email and phone number.

        for phone number
            request:{
                "user_id": "9818051081",
                "ip_add"    : "user ip address" 
            } 
        for email 
            request:{
                 "user_email": "gk.441@gmail.com",
                 "ip_add"    : "user ip address"
            }
    '''    
    try:
        otp=""

        if "user_email" in obj_doc:
            receiver_email = obj_doc["user_email"]
            sender_email   = "gk.411995@gmail.com"
            password       = "12wedfvbabc"

            # logic for seeing whether email ID already exist for our other users or not 
            myQuery = {"user_email":receiver_email}
            
            obj_model.FindOne("USERS", myQuery, proj={"_id":1}, check=True)
            
            #checking error in api log
            if obj_model.obj_logs.var_error == True:
                return 0
            
            otp            = generateOTP()
            result         = SendEmail.SendOtp(sender_email, receiver_email, password, otp)

            if result["status"] != "success":

                obj_model.obj_logs.menthod_log_error(
                    error = {
                        "error_type":"stop",
                        "errroe_msg":result
                     }
                )
                return 0

        if "user_id" in  obj_doc: 

            receiver_phone = obj_doc["user_id"]
            #checking whether record exist or not

            myQuery = {"user_id":receiver_phone}
            
            obj_model.FindOne("USERS", myQuery, proj={"_id":1}, check=True)
            
            #checking error in api log
            if obj_model.obj_logs.var_error == True:
                return 0

            #generating otp, sending messages
            otp     = generateOTP()
            
            result = send_sms.func_sendSms(receiver_phone, "Your otp is : " + otp)
           
            #if sending message fails then logging and returning
            if result["status"] != "success":
                obj_model.obj_logs.menthod_log_error(
                error = {
                    "error_type":"stop",
                    "errroe_msg":result["message"]
                }
                )
                return 0

        #logic for storing and updating the otp with Ip address in OTPS collection in order to verify while doing sign up
        filter = obj_doc
        
        update = {"$set":{**obj_doc,"otp":otp, "last_modified":str(datetime.datetime.now())}}
        
        obj_model.updateOne("OTPS",filter,update,upsert=True) 
        
        #checking error in api log
        if obj_model.obj_logs.var_error == True:
            return 0
        
        if obj_model.obj_logs.var_error == True:
            return 0

        obj_model.obj_logs.method_log_success(
        success = {
            "Msg":"OTP Sent"
        })

        return 1


    except Exception as e:
        obj_model.obj_logs.menthod_log_error(
            error = {
                    "error_type":"stop",
                    "msg":"Sommething went wrong while sending record",
                    "desc":str(e)
                })
        return 0

    return result

# function to generate OTP 
def generateOTP() : 
    # import library 
    import math, random 
    # Declare a string variable   
    # which stores all string  
    string = '0123456789'
    OTP = "" 
    length = len(string) 
    for i in range(5) : 
        OTP += string[math.floor(random.random() * length)] 
        i=i
  
    return OTP 