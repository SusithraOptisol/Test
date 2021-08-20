class Student:
     _name = None
     _roll = None
     _branch = None
    
     def __init__(self, name, roll, branch): 
          self._name = name
          self._roll = roll
          self._branch = branch
     
     def _displayRollAndBranch(self):
          print("Roll: ", self._roll)
          print("Branch: ", self._branch)
 
 
class Teacher(Student):
 
       def __init__(self, name, roll, branch):
                Student.__init__(self, name, roll, branch)
         
       def displayDetails(self):
                print("Name: ", self._name)                                   
                self._displayRollAndBranch()
 
class Admin:
    def __init__(self, name, roll, branch):
                Student.__init__(self, name, roll, branch)
                
    def display(self):
        print("Name: ", self._name)                                   
        self._displayRollAndBranch()
obj1 = Teacher("R2J", 1706256, "Information Technology")
obj1.displayDetails()  #here we will not get any error
obj = Admin("R2J", 1706256, "Information Technology")
obj.display()     #here we will get an error because this is not the drived class of student