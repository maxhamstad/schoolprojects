from Ingredient import Ingredient
from Recipe import Recipe

def main():
    recipe_name = input("What would you like your Recipe to be named? ")
    recipe = Recipe(recipe_name)
    has_ingredients = input("Do you have any ingredients? (yes/no) ").lower()
    
    while has_ingredients == 'yes':
        ingredient_name = input("What is your ingredient name? ")
        grams = float(input(f"How many grams of {ingredient_name} should we add? "))
        calories = float(input("How many calories is that? "))
        
        ingredient = Ingredient(ingredient_name, grams, calories)
        
        recipe.add_ingredient(ingredient)
        
        has_ingredients = input("Do you have another ingredient? (yes/no) ").lower()
        
    needs_baking = input("Does the Bread need to be baked? (yes/no) ").lower()
    
    if needs_baking == 'yes':
        bake_time = float(input("How many minutes does it need to bake? "))
        bake_temp = float(input("What temperature (F) does it need to bake at? "))
        recipe.set_bake_time(bake_time)
        recipe.set_bake_temp(bake_temp)
    servings = float(input("How many servings does this recipe make? "))
    recipe.set_num_servings(servings)
        
    sit_out = input("Does the recipe need to sit out before serving? (yes/no) ").lower()
    if sit_out == 'yes':
        sit_time = float(input("How many minutes does it need to sit out? "))
        recipe.set_sit_time(sit_time) 
    
    print("\nYour recipe is:\n")
    print(recipe)
    
main()