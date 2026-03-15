from characters.character import Character

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 15)
        self.potions = 3
        self.inventory = []  

    def add_item(self,item):
        self.inventory.append(item)
        print(f"{item} added to inventory.")

        def show_inventory(self):
            if self.inventory:
                print("Inventory:")
                for item in self.inventory:
                    print(f"- {item}")
            else:
                print("Inventory is empty.")
                