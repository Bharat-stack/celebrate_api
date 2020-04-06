import json

from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework import status
from rest_framework.decorators import api_view

from Appserver import custom_func
from Appserver import appServer,db_startup_param,validator
from Appserver.api_log import ApiLogs


@api_view(['GET', 'POST'])
def create_user_01(request):

    obj_logs = ApiLogs()    
    if request.method =="POST":
        

        #Get the requested data of new user
        req_body = dict(request.data)
        
        isReqValid = validator.func_validate_create_user_01(req_body)

        if isReqValid != None:
            return JsonResponse({"error":isReqValid})

        #Getting data base parameter parameter for making connections
        db_param = db_startup_param.func_get_db_param("test")

        #setting api endpoint action
        api_action={
            "method":"Appserver.ai_users_01",
            "action":"func_insert_user"
        }

        #wrapping all API parameter which is required for APPSEVER
        api_param = {**db_param, **api_action,"obj_doc":req_body}
        
        #getting object and processing request 
        obj_appserver = appServer.RunApi(obj_logs)

        obj_appserver.method_process_req(api_param)
        
        response = obj_logs.method_get_response()
        
        return JsonResponse(response) # methods must return HttpResponse      
 
@api_view(['GET', 'POST'])
def get_user_01(request):
    
    obj_logs = ApiLogs()
    if request.method =="POST":
       
         #Get the requested data of new user
        req_body = dict(request.data)
        
        if not ("token" in req_body and len(req_body) == 1 and len(req_body["token"]) >10):
            return JsonResponse({"error":{"error_type":"stop", "desc":"invalid req, only token is required"}})

        #get and decode token
        decoded_payload = custom_func.func_decode_custom_token(req_body["token"])
        if "error_type" in decoded_payload:
            return JsonResponse({"error":decoded_payload})
        
        #validate decoded payload 
        if not(len(decoded_payload) == 2 and "user_id" in decoded_payload and len(decoded_payload["user_id"]) > 2   and "user_pass" in decoded_payload and len(decoded_payload["user_pass"])) > 2:
             return JsonResponse({"error":{"error_type":"invalid token", "desc":"invalid payload"}})       

        #Getting data base parameter parameter for making connections
        db_param = db_startup_param.func_get_db_param("test")

        #setting api endpoint action
        api_action={
            "method":"Appserver.ai_users_01",
            "action":"func_get_user_info"
        }

        #wrapping all API parameter which is required for APPSEVER
        api_param = {**db_param, **api_action,"obj_doc":decoded_payload}
       
        #getting object and processing request 
        
        obj_appserver = appServer.RunApi(obj_logs)

        obj_appserver.method_process_req(api_param)
        
        response = obj_logs.method_get_response()

        return JsonResponse(response) # methods must return HttpResponse  

@api_view(['GET', 'POST'])
def send_otp_01(request):
    
    if request.method != "POST":
        return JsonResponse({"error":"Only POST is allowed"})

    obj_logs = ApiLogs()
    if request.method =="POST":
      
         #Get the requested data of new user
        req_body = dict(request.data)
        
        isReqValid = validator.func_validate_send_otp_01(req_body)

        if isReqValid != None:
            return JsonResponse({"error":isReqValid})

       
        #get and decode token
        db_param = db_startup_param.func_get_db_param("test")

        #setting api endpoint action
        api_action={
            "method":"Appserver.ai_sendotp_01",
            "action":"func_SendOtp"
        }

        #wrapping all API parameter which is required for APPSEVER
        api_param = {**db_param, **api_action,"obj_doc":req_body}
      
        #getting object and processing request 
        
        obj_appserver = appServer.RunApi(obj_logs)

        obj_appserver.method_process_req(api_param)
        
        response = obj_logs.method_get_response()
        
        return JsonResponse(response) # methods must return HttpResponse

@api_view(['GET', 'POST'])
def get_token(request):

    if request.method=="POST":
        
        #getting token
        token = custom_func.func_create_custom_token(request.data)
        
        resp_status = {
            "token":token
        }
        
        return JsonResponse(resp_status)

@api_view(['GET', 'POST'])
def get_decoded_token(request):

    if request.method=="POST":
        
        get_token = request.data["token"]
        
        #token_to_decode=reqData.encode("utf-8")
        resp_status = custom_func.func_decode_custom_token(get_token)
        return JsonResponse(resp_status)

@api_view(['GET', 'POST'])
def get_otp(request):

    obj_logs = ApiLogs()

    if request.method=="POST":
        
        req_body = dict(request.data)

        #Getting data base parameter parameter for making connections
        db_param = db_startup_param.func_get_db_param("test")

        #setting api endpoint action
        api_action={
            "method":"ai_sendotp_01",
            "action":"func_SendOtp"
        }

       #wrapping all API parameter which is required for APPSEVER
        api_param = {**db_param, **api_action,"obj_doc":req_body} 
        
        obj_appserver = appServer.RunApi(obj_logs)

        obj_appserver.method_process_req(api_param)
        
        response = obj_logs.method_get_response()

        return JsonResponse(response)
