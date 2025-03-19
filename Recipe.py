from Ingredient import Ingredient
class Recipe:
    def __init__(self, name: str, bake_time: float = 0.0, bake_temp: float = 0.0, num_servings: float = 1, sit_time: float = 0.0):
        if bake_time < 0:
            raise Exception("Bake time must be non-negative.")
        if bake_temp < 0:
            raise Exception("Bake temperature must be non-negative.")
        if num_servings <= 0:
            raise Exception("Number of servings must be positive.")

        self.__name = name
        self.__bake_time = bake_time
        self.__bake_temp = bake_temp
        self.__num_servings = num_servings
        self.__ingredients = []
        self.__sit_time = sit_time
        
    """Sets the bake time for the recipe."""    
    def set_bake_time(self, bake_time: float):
        self.__bake_time = bake_time
        
    """Sets the bake time for the recipe.""" 
    def set_bake_temp(self, bake_temp: float):
        self.__bake_temp = bake_temp
    
    """Sets the number of servings for the recipe."""
    def set_num_servings(self, num_servings: float):
        if num_servings <= 0:
            raise ValueError("Number of servings must be positive.")
        self.__num_servings = num_servings
        
    """Sets the sit time before serving the recipe."""
    def set_sit_time(self, sit_time: float):
        self.__sit_time = sit_time
    
    def add_ingredient(self, ingredient: Ingredient):
        """Adds an ingredient to the recipe."""
        self.__ingredients.append(ingredient)
    
    """Calculates and returns the calories per serving."""
    def get_calories_per_serving(self) -> float:
        total_calories = 0
        for ingredient in self.__ingredients:
            total_calories += ingredient.get_calories()
        return total_calories / self.__num_servings
    
    """Returns a string representation of the recipe."""
    def __str__(self) -> str:
        recipe_info = [self.__name + ":"]
        for ingredient in self.__ingredients:
            recipe_info.append(f"{ingredient.get_grams():.1f} grams of {ingredient.get_name()}")
        if self.__bake_time > 0 and self.__bake_temp > 0:
            recipe_info.append(f"Bake at {self.__bake_temp}°F for {self.__bake_time} minutes.")
        elif self.__bake_time > 0 and self.__bake_temp == 0:
            recipe_info.append(f"Let sit for {self.__bake_time} minutes.")
        if self.__sit_time > 0:
            recipe_info.append(f"Let sit for {self.__sit_time} minutes.")
            
        recipe_info.append(f"{self.get_calories_per_serving():.1f} Calories per serving")
        return "\n".join(recipe_info)
