
from email import message
from reg import db
from reg import users
import random
import string
def createUser(name=None,email=None,password=None):
    try:
        user_to_create = users(name=name,
                            email=email,
                            password=password)
        db.create_all()                            
        db.session.add(user_to_create)
        db.session.commit()
        return responseHandler(True,{},"User creatation is done")
    except Exception as e:
        if (str(e.__cause__)=="UNIQUE constraint failed: users.email"):
            return responseHandler(False,{},"Email already existed") 
        else : 
            return responseHandler(False,{},str(e.__cause__))

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def responseHandler(status=None,data=None,message=None) :
    return { "status":status,"data":data,"message":message}

