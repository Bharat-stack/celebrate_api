from getConnection import Connection 
from insertUsers import createUsers

conn = Connection()
conn = conn.getConnection(host="localhost",port=27017,dbName="celebrate")

db=conn[2]
query={
  'collMod': 'users',
  'validator': {
    '$jsonSchema': {
      'bsonType': 'object',
      'required': ['FirstName', 'LastName', 'user_id', 'password'],
      'properties': {
        'FirstName': {
          'bsonType': 'string',
          'description': 'must be a string and is required'
        },
        'LastName': {
          'bsonType': 'string',
          'description': 'must be a string and is required'
        },
        'user_id': {
          'bsonType': 'string',
          'description': 'must be a string and is required'
        },
        'password': {
          'bsonType': 'string',
          'description': 'must be a string and is required'
        },
      }
    }
  },
  "validationAction": 'error'
}

result=db.command(query)
print(result)