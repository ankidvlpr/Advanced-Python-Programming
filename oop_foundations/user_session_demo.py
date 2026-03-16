"""Mini user-session example with login, logout, and simple checks."""

class UserSession:

    def __init__(self, user_id):
        self.user_id = user_id
        self.is_active = False
        self.token = None


    def login(self, token):
        # A token must be long enough before the session becomes active.
        if len(token) < 8:
            raise ValueError("token too short")
        
        self.token = token
        self.is_active = True
        return True
        
    def logout(self):
        self.is_active = False
        self.token = None

    def to_dict(self):
        return {
            "user_id" : self.user_id,
            "is_active" : self.is_active,
            "token" : self.token
        }
    
    

    



    
# Manual test flow for the session object.
i = UserSession("user_43")

# test1  : short token should fail

try:
    i.login("abc")
    assert False
except ValueError:
    assert True

# test2 : valid token works
i.login("assjjsjs")
assert i.is_active == True

# test 3: logout clears token

i.logout()
assert i.token == None

print(i.to_dict())
