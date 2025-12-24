class Form:
    clg_name="CGU"
    clg_phone="1234567890"
    def __init__(self,name,p,a=20):
        self.name=name
        self.phone=p
        self.age=a
    def greet(self):
        print(f"Hello {self.name}")
s1=Form("Nani","123",12)
s2=Form("Azzu","5678")
print(s2.name)
s2.name="Aakshat"
print(s2.name)
s2.greet()