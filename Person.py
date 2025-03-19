class Person:
    """demonstrating writing a class definition fo a person with a favorite number and a name
    """
    def __init__(self, name:str, fav_num:int):
        self._name:str = name
        self._fav_num:int = fav_num
    
    def __str__(self) -> str:
        #str function converts any number into a str of a number 
        return str(self._name + " has a favorite number of " + str(self._fav_num))
        
    def get_name(self):
        """ returns the name of the person """
        return self._name
    
    def set_name(self, name:str) -> None:
        if not name is None and name != "":
            self._name = name
            
    def get_fav_num(self) -> int:
        return self._fav_num
    
    def set_fav_num(self, fav_num:int) -> None:
        self._fav_num = fav_num

#all the way to the left indentation
def main():
    ann:Person = Person("Ann", 14)
    bob:Person = Person("Bob", 55)
    chuck:Person = Person("Chuck", 24)
    
  #  print(ann.get_name())
  #  print(chuck.get_name())
    print(ann)
    ann.set_name("Annabelle")
    #print(ann.get_name())
    print(ann)
    #print(chuck)
main()