class Point:

    #this is a constructor where the variables are initialized using the __init__
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y

    #This is a destructor where the pointer is deleted using the __del__
   def __del__(self):
      class_name = self.__class__.__name__
      print class_name, "destroyed"


pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3) # prints the ids of the obejcts
del pt1
del pt2
del pt3

# Note: Ideally, you should define your classes in separate file, then you should import them in your main program file using import statement.