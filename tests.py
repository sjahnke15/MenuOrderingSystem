import unittest
from order_processor import OrderProcessor

# Testing done on the OrderProcessor module because ordering.py (main) uses this module to 
#   print the output.

class Testing(unittest.TestCase):
    proc = OrderProcessor()
    meal_menu = {
            "main": {
                "1": "Eggs",
                "4": "Waffles"
            },
            "side": {
                "2": "Toast",
                "10": "Bacon" 
            },
            "drink": {
                "3": "Coffee"
            }
    }

    # The createItemDict method on a different menu to ensure correct behavior
    def test_CreateItemDict(self):
        
        food = ["1", "2", "3", "4", "10"]
        expectedOutput = {
            "main": ["Eggs", "Waffles"],
            "side": ["Toast", "Bacon"], 
            "drink": ["Coffee"],
            "dessert": []
        } 
        actualOutput = self.proc.createItemDict(food, self.meal_menu)
        self.assertEqual(actualOutput, expectedOutput) 

        food = ["1", "2", "3", "4", "10.9"]
        actualOutput = self.proc.createItemDict(food, self.meal_menu)
        self.assertEqual(actualOutput, "Unable to process: All IDs in order need to be a digit")

        food = ["1", "2", "3", "4", "11"]
        actualOutput = self.proc.createItemDict(food, self.meal_menu)
        self.assertEqual(actualOutput, "Unable to process: Unrecognized item ID (11)")

    # Test the 10 given requirements
    def test_process(self):
        # 1. An order consists of a meal and collection of comma separated item Ids.
        input = "Breakfast 1 2 3"
        self.assertEqual(self.proc.process(input), "Unable to process: Input formatted incorrectly")
        # 2. The system should return the name of the items ordered
        input = "Breakfast 1,2,3"
        self.assertEqual(self.proc.process(input), "Eggs, Toast, Coffee")
        # 3. The system should always return items in the following order: meal, side, drink
        input = "Breakfast 3,2,1"
        self.assertEqual(self.proc.process(input), "Eggs, Toast, Coffee")        
        # 4. If multiple items are ordered, the number of items should be indicated
        input = "Lunch 1,2,2,2,2,2,2,2,3"
        self.assertEqual(self.proc.process(input), "Sandwich, Chips(7), Soda")        
        # 5. Each order must contain a main and a side
        input = "Breakfast 1,3"
        self.assertEqual(self.proc.process(input), "Unable to process: Missing a side")
        input = "Breakfast 2,3"
        self.assertEqual(self.proc.process(input), "Unable to process: Missing a main dish")
        # 6. If no drink is ordered, water should be returned
        input = "Breakfast 1,2"
        self.assertEqual(self.proc.process(input), "Eggs, Toast, Water")        
        # 7. At breakfast, multiple cups of coffee can be ordered
        input = "Breakfast 1,2,3,3,3,3,3"
        self.assertEqual(self.proc.process(input), "Eggs, Toast, Coffee(5)")       
        input = "Lunch 1,2,3,3,3,3,3"
        self.assertEqual(self.proc.process(input), "Unable to process: Cannot order multiple drinks at Lunch")      
        # 8. At lunch, multiple sides can be ordered
        input = "Breakfast 1,2,2,3"
        self.assertEqual(self.proc.process(input), "Unable to process: Cannot order multiple sides at Breakfast")
        input = "Lunch 1,2,2,3"
        self.assertEqual(self.proc.process(input), "Sandwich, Chips(2), Soda")
        # 9. At dinner, dessert must be ordered
        input = "Dinner 1,2,3"
        self.assertEqual(self.proc.process(input), "Unable to process: Must order Dessert at Dinner")
        # 10. At dinner, water is always provided
        input = "Dinner 1,2,3,4"
        self.assertEqual(self.proc.process(input), "Steak, Potatoes, Wine, Water, Cake")

if __name__ == '__main__':
    unittest.main()