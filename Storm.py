class Storm:
    
    def __init__(self, precip: str, inches: float, hours: float):
        self._precip = "snow"
        if self._precip != "snow":
            self._precip = precip
            
        self._inches = 0
        if inches > 0:
            self._inches = inches
            
        self._hours = 1
        if hours > 1:
             self._hours = hours
        
    def get_precip(self):
        """ returns the name of precipitation """
        return self._precip
    
    def set_precip(self, precip:str) -> None:
        if not precip is None and precip != "":
            self._precip = precip
            
    def get_inches(self) -> float:
        return self._inches
    
    def set_inches(self, inches:float) -> None:
        if not inches < 0: 
            self._inches = inches
        
    def get_hours(self) -> float:
        return self._hours
    
    def set_hours(self, hours:float) -> None:
       if hours > 0: 
            self._hours = hours
            
    def __str__(self):
        return ("This storm dropped " + str(self._inches) + " inches of rain over the course of " + str(self._hours) + " averaging " + str(self.get_precip_per_hour()) +" inches per hour.") 

    def get_precip_per_hour(self):
        return (self._inches / self._hours)
def main():
    # create a Storm object
    gentle_rain: Storm = Storm("rain", 1.5, 3)
    # This will trigger an automatic call to Storm.__str__()
    print(gentle_rain)
    # Try to change a value using the setter method
    gentle_rain.set_inches(2.5)
    # Make sure it changed
    print(gentle_rain)

    print("Testing a few getter methods:")
    print(gentle_rain.get_precip() + " "
          + str(gentle_rain.get_inches()) + " "
          + str(gentle_rain.get_hours()))
    print(gentle_rain.get_precip_per_hour())

    storm_of_century = Storm("snow", 48, 36)
    print(storm_of_century)
    
    storm_of_century.set_hours(48)
    print(storm_of_century)
    
main()
        

