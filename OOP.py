# =============================================================================
# OBJECT ORIENTED PROGRAMMING
# =============================================================================

class garden:
    def buildings(self,height,floors):
        print("Restaurant")
        

obj_1=garden()

print(type(obj_1))

obj_1.buildings(20,20)


# =============================================================================
# Attributes and Methods
# =============================================================================

class student:
    def __init__(self,breed):
        self.breed=breed
        print("I am working fine")
    
    def meth(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
    
    def meth_2(self):
        self.meth("Hamza",22)
    

obj_1=student("Lab")
obj_2=student("German")

obj_1.meth("Hamza", 22)
obj_2.meth("Gulshan",21)

obj_1.meth_2()
obj_2.meth_2()
print(obj_1.name)


# =============================================================================
# Inheritance
# =============================================================================

class first:
    def meth_1(self):
        print("meth_1")
    def meth_2(self):
        print("meth_2")
        
        
class second:
    def meth_3(self):
        print("meth_3")
    def meth_4(self):
        print("meth_4")
        
class third(first,second):
    def meth_5(self):
        print("meth_5")
    def meth_6(self):
        print("meth_6")


second = second()
 

third = third()
third.meth_1()

# =============================================================================
# EXAMPLES
# =============================================================================

class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth=breadth
        
    def area(self):
        print(self.length*self.breadth)
        
    def perimeter(self):
        print(2*(self.length+self.breadth))

class circle:
    def __init__(self):
        print("circle init")
        
        
class square(rectangle,circle):
    def __init__(self,side):
        super().__init__(side, side)
        super(rectangle,self).__init__() #calling all constructors after rectangle till the end
        
        
        
sq =square(5)
sq.area()
sq.perimeter()

# =============================================================================
# Polymorphism
# =============================================================================

(class rectangle:
    
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
        
    def area(self):
        print(self.length*self.breadth)
        
class square:
    def __init__(self,side):
        self.side=side
    
    
    def area(self):
        print(self.side**2)
        
        
rec = rectangle(10,15)
sq = square(10)

for shape in (rec,sq):
    shape.area()
