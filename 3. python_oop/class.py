# class is the blue print 
# object is the real thing or its an instance of class

class Car:
 def  __init__(self,name):
    self.name = name

car1 =Car('bmw')
car2 = Car('benz') 

# print(car1.name)
# print(car2.name)


# -----------------------------------------

class Document:
  def __init__(self,text,source):
    self.text = text
    self.source=source

lang1 = Document('python','online source')

lang2 = Document('java','hand written notes')

# print(lang1.text,':',lang1.source)
# print(lang2.text,':',lang2.source)



# -----------------------------------------------------
#Class variable : for all object, instance variable: for specific object
class Document:
  rank = 'one'
  def __init__(self,text,source):
    self.text = text
    self.source=source

lang1 = Document('python','online source')

lang2 = Document('java','hand written notes')

print(lang1.text,':',lang1.source)
print(lang2.text,':',lang2.source)