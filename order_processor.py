import json

# Helper so I don't have to keep rewriting "Unable to process"
def errorMessage(message):
    return "Unable to process: " + message

class OrderProcessor():
    def __init__(self):
        # The list of supported meals
        self.meals = ['Breakfast', 'Lunch', 'Dinner']
        
        # Load in the menu from the json file. menu.json should always be in the same directory as this file
        try:
            with open("menu.json") as menuFile:
                self.menu = json.loads(menuFile.read())

        except Exception as e:
            print("Error loading the menu from menu.json. Make sure menu.json is located in the same directory!")
            exit()

    # Processes an order and returns the appropriate output
    def process(self, order: str) -> str:

        orderCpy = order.split() # Split the order string into individual pieces
        if(len(orderCpy) > 2):
            return errorMessage("Input formatted incorrectly")
        mealName = orderCpy[0]

        if mealName not in self.meals:
            return errorMessage("Meal name is not supported")

        try:
            food = orderCpy[1]
        except IndexError:
            # Dinner is missing dessert too, so need to check which one it is (already knowing it is valid)
            if mealName == "Dinner": 
                return errorMessage("Main is missing, Side is missing, Dessert is missing")
            else:
                return errorMessage("Main is missing, Side is missing")

        meal_menu = self.menu[mealName]
        food = food.split(',')

        dict = self.createItemDict(food, meal_menu)
        if type(dict) == str: # Then it is an error message
            return dict

        # All meal types require these checks
        if not dict['main']:
            return errorMessage("Missing a main dish")

        if not dict['side']:
            return errorMessage("Missing a side")

        if len(dict['main']) > 1:
            return errorMessage("Cannot order multiple main dishes")

        # Make specific meal checks
        ##### BREAKFAST #####
        if mealName == "Breakfast": 
            if len(dict['side']) > 1:
                return errorMessage("Cannot order multiple sides at Breakfast")

            if not dict['drink']:
                dict['drink'].append("Water")

        ###### LUNCH ######
        elif mealName == "Lunch":
            if not dict['drink']:
                dict['drink'].append("Water")
            elif len(dict['drink']) > 1:
                return errorMessage("Cannot order multiple drinks at Lunch")

        ##### DINNER #####
        elif mealName == "Dinner":
            if len(dict['side']) > 1:
                return errorMessage("Cannot order multiple sides at Dinner")

            if len(dict['drink']) > 1:
                return errorMessage("Cannot order multiple drinks at Dinner")
            
            if not dict['dessert']:
                return errorMessage("Must order Dessert at Dinner")
            
            dict['drink'].append("Water")

        return self.dictToString(dict, mealName)

    # Returns a dictionary containing the items in the order
    def createItemDict(self, food, meal_menu):
        # Add ordered items to a dict, if an ID is not valid, return an error message
        dict = {
            'main': [],
            "side": [],
            "drink": [],
            "dessert": []
        }

        for id in food:
            valid = False
            if not id.isdigit():
                return errorMessage("All IDs in order need to be a digit")
            else:
                for mealtype in meal_menu.keys():
                    if id in meal_menu[mealtype].keys():
                        dict[mealtype].append(meal_menu[mealtype][id])
                        valid = True
                if not valid:
                    return errorMessage("Unrecognized item ID (" + id + ")" )

        return dict

    # Formats the dict generated in the process() method to the required output
    def dictToString(self, dict, mealName):
        # This method is only called if the order is valid
        retString = ""

        # Format main items
        retString += dict['main'][0] + ", "

        # Format side items
        retString += dict['side'][0]
        sideCount = dict['side'].count(dict['side'][0])
        if sideCount > 1:
            retString += ("(" + str(sideCount) + ")")
        retString += ", "

        # Format drink items
        retString += dict['drink'][0]
        drinkCount = dict['drink'].count(dict['drink'][0])
        if drinkCount > 1:
            retString += ("(" + str(drinkCount) + ")")
        if mealName == "Dinner" and dict['drink'][0] != 'Water':
            retString += ", Water"

        # Format dessert items
        if not dict['dessert']:
            return retString
        else:
            retString += ", " + dict['dessert'][0]

        return retString