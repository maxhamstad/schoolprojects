#notes for class

"""Wed/Nov/13"""
#classes are data types: int and float already exist in data types, if you have something that doesn't exist combine some existing data types to make a new data type

#Attribute details: attributes are variables that belong to a entire object, declare it in __init__()...all code in this class can access attributes not just one function
##class defines what attributes are, each object maintains seperate values for those attributes each instance of the class has seperate memory

#private attributes: Rule of thumb, make attributes private, self._ssn(name starts with underscore)... only the current class is allowed direct access to private attribures 
##your public methods can perform safty checks instead of just allowing any change to happen

#Terminology: methods of functions: functions: take inputs  and return outputs, when function is finished running that the end
##Methods: can read and change attributes for a given object, when a method is done runnning the attribute values stick around until the next method execution

"""__init__(self)""" #pythons version of a constructor method, special method that builds a object from the class
## python rules: must start and end with double underscore around "init", can have parameters for attribute starting values
## You define this method, but you never call it yourself!
## What does it do ? It gives good starting values to all attributes, hopefully based on parameters passed in, or good default values that dont leave you in bad state

"""#Self"""#: Why do we keep using self in our code ?
#you can have 1 class but multiple objects
##each object owns its own copy of each attribute and method
## when method is called pyhton will let you know whcih specific object is involved

#local variable vs. Attribute: if you have attribute and a local variable with the same name, the local varaible takes priority

#methods: are the actions that an object can take, every method in a class has access to all of the attributes plus any input parameters for that method

#Getters and setters: two types of methods commonly seen in class
#gatekeepers of a objects attributes, if a outsider needs to know what is stores, provide a getter method that returns value
##if a outsider needs to change whats being stores provide a setter method that can change a variables value

"""Mon/2/Dec"""
#reading and writing files, want data to survive after program stops exacuting
#Text files vs. Binary- Text: pro human and readable, con is larger file size- Binary:

#creating a file objectm open file in desirable mode, r for reading, w for writing, a for append
#example: my_file = open('filename', 'w') this open method contains all the useful data and methods related to reading and writing the file you specified 