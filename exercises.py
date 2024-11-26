# Exercise 0 

def example_list_function():
  example_list = ['element1', 'element2', 'element3']
  for element in example_list:
      print(element)

# Call the function and print each element
example_list_function()

print('------------------------')

# Exercise 1 

def manage_students():
    students = ["Israa", "Layla", "Fatima"]
    first_student = students[1]
    last_student = students[-1]
    return first_student , last_student

# Call the function and print the result
print('Exercise 1:', manage_students())

print('------------------------')

# Exercise 2

def combine_foods():
    foods = ("Pizza", "Burger", "Salad")  
    meal = ""  

    for food in foods:
        meal += food + " "

    return meal

print('Exercise 2:', combine_foods())

print('------------------------')

# Exercise 3

def slice_foods():
    foods = ("Pizza", "Burger", "Salad")
    last_two_foods = foods[-2:]  
    return last_two_foods


print('Exercise 3:', slice_foods())

print('------------------------')

# Exercise 4

def hometown_info():
    home_town =  {
        'city': 'New York City',
        'state': 'New York',
        'population': 8336817
    }

    home_town_message = (f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

    return home_town_message

print('Exercise 4:', hometown_info())

print('------------------------')

# Exercise 5 

def list_home_town_items():

    home_town =  {
        'city': 'New York City',
        'state': 'New York',
        'population': 8336817
    }

    home_town_items = []
    for key in home_town:
        home_town_items.append(f"{key} = {home_town[key]}")
    
    return home_town_items

print('Exercise 5:', list_home_town_items())

