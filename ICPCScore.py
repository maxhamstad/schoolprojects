
class ICPCScore: 

    def __init__(self, name: str, points: int, minutes: int, last_accepted: int):
        self._name = name
        self._points = points
        self._minutes = minutes
        self._last_accepted = last_accepted
        
    """Returns the name."""
    def get_name(self):
        return self._name
    
    """Sets the name."""
    def set_name(self, name:str) -> None:
        if not name is None and name != "":
            self._name = name
            
    """Returns the points"""        
    def get_points(self):
        return self._points
    
    """Sets the points."""
    def set_points(self, points:int) -> None:
        if points > 0: 
            self._points = points
        else:
            raise ValueError("Points cannot be negative")
    
    """get the minutes"""        
    def get_minutes(self):
        return self._minutes
    
    """Sets the minutes"""
    def set_minutes(self, minutes:int) -> None:
        if minutes > 0: 
            self._minutes = minutes
        else:
            raise ValueError("minutes cannot be negative")
    def __str__(self) -> str:
        return str(f"{self._name} scored {self._points} points and had {self._minutes} minutes total time.")
    