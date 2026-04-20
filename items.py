class Item:

    def __init__(self, name, quantity, description, weight):
        self.name = name
        self.quantity = quantity
        self.description = description
        self.weight = weight

    def __str__(self):
        return (
            f"Item name: {self.name}\n"
            f"Item quantity: {self.quantity}\n"
            f"Item description: {self.description}\n"
            f"Item weight: {self.weight}"
        )
