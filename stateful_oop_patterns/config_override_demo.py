"""Practice file showing class variable vs instance override behavior."""

class Config:
    ENV = "Production"

    def __init__(self, overrides=None):
        
        if overrides is None:
            overrides = {}

        self.ENV = Config.ENV

        # Instance-level override wins only for this object.
        if "ENV" in overrides:
            self.ENV = overrides["ENV"]
    
# Compare old and new objects after changing the class variable.
c1 = Config()
print(c1.ENV)

Config.ENV = "staging"

c2 = Config()
print(c2.ENV)



print(c1.ENV)
