from Person import Person


def main():
    ann:Person = Person("Ann", 14)
    bob:Person = Person("Bob", 55)
    chuck:Person = Person("Chuck", 24)
    
    print(ann.get_name())
    print(chuck.get_name())
    
    ann.set_name("Annabelle")
    print(ann.get_name())
    
main()