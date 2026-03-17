"""Mixin pipeline example to understand super() and MRO order."""

class Base:
    
    def process(self, data):
        print("Base processing")
        return data


class AuthMixin:
    
    def process(self, data):
        # First layer checks required auth token.
        print("auth check")
        if 'token'  not in data:
            raise ValueError("no token")
        return super().process(data)

        

class TransformMixin:
    
    def process(self,data):
        # Second layer mutates payload before base processing.
        print("data is transformed")
        data['tranform'] = True
        return super().process(data)



class App(AuthMixin, TransformMixin , Base):
    pass

# Demo: call chain follows App MRO.
app = App()
result = app.process({'token' : 'abc123', 'value' : 42})

print(result)

print(App.__mro__)
