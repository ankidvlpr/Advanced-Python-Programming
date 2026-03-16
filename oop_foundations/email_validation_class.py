"""Email helper class for basic validation and parsing practice."""

class Email:

    def __init__(self, address):
        # Keep validation simple: just check the common required symbols.
        if "@" not in address or "." not in address:
            raise ValueError("not valid email")
        
        self.address = address

    def split_email(self):
        # Split once so local and domain parts can be reused by other methods.
        return self.address.split("@")
    
    def local_name(self):
        part = self.split_email()
        return part[0]
    
    def domain_name(self):
        part = self.split_email()
        return part[1]
    
    def __repr__(self):
        return f"Email({self.address})"

        
# Small example showing parsing output.
email = Email("ankit@gmail.com")
print(email.domain_name())
print(email.local_name())
# print(email.address)
print(email)
        
        
