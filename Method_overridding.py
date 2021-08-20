class A:
    
    def calc(self,a,b):
        Result = a+b
        return Result

class B(A):
    def calc(self,a,b): #this calc method overrides the predefined method in parent class
        Result = a*b
        return Result
        

a1 =B()
print("Result is" , a1.calc(3,6))