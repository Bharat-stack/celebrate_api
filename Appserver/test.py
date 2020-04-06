import json

def compare_object(a,b):   
    if type(a) != type (b):      
        return False   
    elif type(a) is dict:      
        return compare_dict(a,b)   
    elif type(a) is list:
        return compare_list(a,b)
    else:      
        return type(a) == type (b)

def compare_dict(a,b):   
    if len(a) != len(b):
        #check whether lenghth is mendatory      
        return False   
    else:      
        for k,v in a.items():         
            if not k in b:
                print(k)       
                return False         
            else:            
                if not compare_object(v, b[k]):               
                    return False   
    return True

def compare_list(a,b):   
    if len(a) != len(b):      
        return False   
    else:      
        for i in range(len(a)):         
            if not compare_object(a[i], b[i]):            
                return False   
    return True

a = '''   
    {      
        "trueKey":true,      
        "falseKey":false,      
        "arrayKey":[0,1,4],      
        "objectKey":{         
            "myKey1":"myVal",         
            "myKey2":"myVal2",         
            "myKey3":"myVal3",         
            "myKey4":"myVal4"      
        }   
    }   
'''
b = '''
    {    
        "falseKey":false,  
        "trueKey":true,           
        "arrayKey":[0,1,90],      
        "objectKey":{         
            "myKey1":"myVal1",         
            "myKey2":"myVal2",         
            "myKey3":"myVal3",         
            "myKey4":"myVal4"      
        }   
    }   
'''
json_a = json.loads(a)
json_b = json.loads(b)
print(compare_object(json_a, json_b))