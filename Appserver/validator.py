import re 

def func_validate_send_otp_01(obj_doc):

    api_req = {
        "reqSampleForSms":{
            "user_id":"989787878",
            "user_ip":"132312qdasdd"
        },
        "reqSampleForEmail":{
            "user_email":"asdshasdh@gmail.com",
            "user_ip"   :"767687hjasjh"
        }
    }

    if len(obj_doc) != 2:
        return {"error_type":"stop","desc":"only two keys are required", **api_req}

    if not(("user_id" in obj_doc or "user_email" in obj_doc) and "user_ip" in obj_doc and len(obj_doc["user_ip"]) > 0):
        return {"error_type":"stop","desc":"invalid request keys or empty values", **api_req}
    
    if ("user_id" in obj_doc and not(func_isvalidephone(obj_doc["user_id"]))) or  len(obj_doc["user_id"]) <= 10:
        return {"error_type":"stop","desc":"Invalid Phone number", **api_req}

    if "user_email" in obj_doc and not(func_isvalidemail(obj_doc["user_email"])):

        return {"error_type":"stop","desc":"Invalid email", **api_req}
    
    return None

def func_validate_create_user_01(obj_doc):
    
    api_req={
        "reqSample":{
        "user_id":"989829122",
        "user_pass":"adasdasd",
        "user_ip":"dasdasdas",
        "otp"    :    "213"
        }
    }

    if len(obj_doc) != 4:
        return {"error_type":"stop","desc":"only four keys are required", **api_req}
    
    if not("user_id" in obj_doc and "user_pass" in obj_doc and "user_ip" in obj_doc and len(obj_doc["user_ip"]) > 0 and "otp" in obj_doc and len(obj_doc["otp"]) > 2,):
        return {"error_type":"stop","desc":"invalid request keys or empty values", **api_req}
    
    if len(obj_doc["user_pass"]) < 5:
        return {"error_type":"stop","desc":"Invalid password, must be greater than 5", **api_req}       
    
    if ("user_id" in obj_doc and not(func_isvalidephone(obj_doc["user_id"]))) or len(obj_doc["user_id"]) <= 10:
        return {"error_type":"stop","desc":"Invalid Phone number", **api_req}

    return None


# Define a function for 
# for validating an Email 
def func_isvalidemail(email):  

    regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    # pass the regualar expression 
    # and the string in search() method 
    if(re.search(regex,email)):  
        return True  
          
    else:  
        return False

def func_isvalidephone(s): 
      
    # 1) Begins with 0 or 91 
    # 2) Then contains 7 or 8 or 9. 
    # 3) Then contains 9 digits 
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}") 
    return Pattern.match(s)         