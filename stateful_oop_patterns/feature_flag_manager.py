"""Feature flag practice with per-instance flag storage."""

class FeatureFlagManager:
    
    
    def __init__(self):
        self.flags = {}

    def turn_on(self, flag_name, users=None):
        self.flag_name = flag_name
        
        # If no user list is given, enable the flag for everyone.
        if users is None:
            self.flags[flag_name] = "ALL"
        else:
            self.flags[flag_name] = users


# Two separate objects keep their own flag state.
a = FeatureFlagManager()
b = FeatureFlagManager()

a.turn_on("Dark mode", ["u1","u2"])
b.turn_on("Dark mode")

print("Message", a.flags)
print("Message", b.flags)


    
