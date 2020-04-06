class ApiLogs:

    obj_error    = ""
    var_error    = False
    obj_recieved = ""
    obj_success = ""
    obj_returned = "" 
    obj_response = ""
    obj_conn     = ""
    obj_client   = ""
    var_warning  = False

    def menthod_log_error(self, **kwargs):
        
        self.obj_error = kwargs
        temp = self.obj_error["error"]

        if temp["error_type"] == "stop" or temp["error_type"] == "fatal":
            self.var_error = True
        elif temp["error_type"] == "warning":
            self.warning = True    
    
    def method_log_success(self, **kwargs):

        self.obj_success = kwargs
        
        if "success" in kwargs:
            self.obj_returned = kwargs["success"]

    def method_send_parameter(self, **kwargs):

        self.obj_recieved = kwargs

    def method_reurned_parameter(self, **kwargs):

        self.obj_returned = kwargs
        #self.var_error    = False

    def method_get_response(self,**kwargs):
        
        #print("apiLog", self.var_error, dict(self.obj_error), self.obj_success)
        if self.var_error == True:
           return  dict(self.obj_error)
        elif self.var_warning == True:
           return dict({**self.obj_success,**self.obj_error})
        else:
            return dict(self.obj_success)   
        




       
