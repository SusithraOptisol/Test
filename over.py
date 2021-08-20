class A:
    
    def calc(self,a,b):
        Result = a+b
        return Result

class B(A):
    def calc(self,a,b): #this calc method overrides the predefined method in parent class
        Result = a*b
        return Result