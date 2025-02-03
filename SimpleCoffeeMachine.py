with open("ingredients.txt","w") as ingredient_file:
    ingredient_file.write("{'caffeine': 5000, 'water': 5000, 'cup': 20, 'sugar': 500, 'milk': 1000, 'tea': 500}")
ingredient_file.close()
recipe_list = {'espresso' : {"caffeine":9,"water":30,"cup":1}, 'flat_white' : {"milk":130,"water":30,"caffeine":9,"cup":1}, 'tea' : {"tea":2, "water":300, "cup":1}}
with open("recipes.txt","w") as recipes_file:
    recipes_file.write(str(recipe_list))

import time
import ast
class CoffeeMachine:
    file2 = open('recipes.txt', 'r')
    file_read2 = file2.read()
    recipies_dict = ast.literal_eval(file_read2)

    def __init__(self, balance):
        self.balance = balance

    def main_menu(self):
        choice = int(input("Choose your drink:\n1) Espresso (3,20$)\n2) Flat White (3$)\n3) Black Tea (2$)\n4) Exit\n"))
        file = open('ingredients.txt', 'r')
        file_read = file.read()
        ingredients_available_dict = ast.literal_eval(file_read)
        if choice == 1:
            if self.balance >= 3.2:
                for i in list(self.recipies_dict["espresso"].keys()):
                    if i in list(ingredients_available_dict.keys()):
                        if ingredients_available_dict[i] >= self.recipies_dict["espresso"][i]:
                            ingredients_available_dict[i] = ingredients_available_dict[i] - self.recipies_dict["espresso"][i]
                        elif ingredients_available_dict[i] < self.recipies_dict["espresso"][i]:
                            print(f"We ran out of {i}")
                            self.main_menu()
                            break
                print("Making...")
                time.sleep(2)
                print("Done!")
                with open("ingredients.txt","w") as file:
                    file.write(str(ingredients_available_dict))
                self.main_menu()

            else:
                print("Not enough money!")
        elif choice == 2:
            if self.balance >= 3:
                for i in list(self.recipies_dict["flat_white"].keys()):
                    if i in list(ingredients_available_dict.keys()):
                        if ingredients_available_dict[i] >= self.recipies_dict["flat_white"][i]:
                            ingredients_available_dict[i] = ingredients_available_dict[i] - self.recipies_dict["flat_white"][i]
                        elif ingredients_available_dict[i] < self.recipies_dict["flat_white"][i]:
                            print(f"We ran out of {i}")
                            self.main_menu()
                            break
                print("Making...")
                time.sleep(2)
                print("Done!")
                with open("ingredients.txt","w") as file:
                    file.write(str(ingredients_available_dict))
                self.main_menu()
            else:
                print("Not enough money!")
            self.main_menu()
        elif choice == 3:
            if self.balance >= 2:
                for i in list(self.recipies_dict["tea"].keys()):
                    if i in list(ingredients_available_dict.keys()):
                        if ingredients_available_dict[i] >= self.recipies_dict["tea"][i]:
                            ingredients_available_dict[i] = ingredients_available_dict[i] - self.recipies_dict["tea"][i]
                        elif ingredients_available_dict[i] < self.recipies_dict["tea"][i]:
                            print(f"We ran out of {i}")
                            self.main_menu()
                            break
                print("Making...")
                time.sleep(2)
                print("Done!")
                with open("ingredients.txt", "w") as file:
                    file.write(str(ingredients_available_dict))
                self.main_menu()

            else:
                print("Not enough money!")
                self.main_menu()
        elif choice == 4:
            print("Exiting...")
            time.sleep(2)
            exit()
        else:
            print("Invalid input!")
            self.main_menu()

user = CoffeeMachine(int(input("Insert Cash: ")))
user.main_menu()
