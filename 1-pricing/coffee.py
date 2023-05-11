# Control the printing format of the item price breakdown
LEFT_ALIGN = 50     # Item name, topping, option,...
RIGHT_ALIGN = 0     # Price tag


class Item:
    """
    An abtract class plays as a boiler plate for an item where it should have a base price and 
    methods to calculate the item price and display the price breakdown of the item.
    """

    BASE_PRICE = None
    NAME = None

    def calculatePrice(self) -> float:
        """Calculate the total price of the item."""
        return self.BASE_PRICE

    def displayPriceBreakdown(self) -> None:
        """Print out the price breakdown of the item."""
        print(
            f"{f'{self.NAME}':<{LEFT_ALIGN}}{f'${self.BASE_PRICE:.2f}':>{RIGHT_ALIGN}}")


class Drink(Item):
    """
    An abstract class which has all the common attributes and methods for drinks.
    """

    BASE_PRICE = 2.0
    SIZE = {"S": 0.0, "M": 0.5, "L": 1.0, "XL": 1.5}
    TOPPING = {"Whipped cream": 0.5}
    MILK_OPTION = {"Whole milk": 0.0, "Almond milk": 0.5}

    # The price adjustment is the extra cost the customers need to pay for a specific type of drink
    # For example:
    #   - Base price: $2 for a small hot drink without cream
    #   - Price adjustments: $1 for blended drinks
    # This is equivalent to price adjustment of hot and cold drinks is $0 and price adjustment of blended drinks is $1
    PRICE_ADJUSTMENT = 0.0

    def __init__(self, size: str, hasWhippedCream: bool, milkOption: str = None):
        # Size
        size = size.upper()
        assert (
            size in self.SIZE), f"Size {size} is not available for {self.DRINK_TYPE}."
        self.size = size

        # Whipped cream topping
        self.hasWhippedCream = hasWhippedCream

        # Milk option
        if milkOption:
            milkOption = milkOption.capitalize()
            assert (milkOption in self.MILK_OPTION), "Invalid milk option"
        self.milkOption = milkOption

    def calculatePrice(self) -> float:
        """Calculate the total price of the Drink."""

        whippedCreamPrice = self.TOPPING["Whipped cream"] if self.hasWhippedCream else 0
        milkOptionPrice = self.MILK_OPTION[self.milkOption] if self.milkOption else 0

        # Compare to Item class which has only the base price,
        # Drink class has to taken into account more options:
        #   - Whipped cream: True - $0.5, False - $0
        #   - Milk: almond - $0.5, whole - $0,...
        #   - Price adjustment: hot - $0, cold - $0, blended - $1,...
        #   - Size: S - $0, M - $0.5,...
        return super().calculatePrice() + whippedCreamPrice + milkOptionPrice + \
            self.PRICE_ADJUSTMENT + self.SIZE[self.size]

    def displayPriceBreakdown(self) -> None:
        """Display the price breakdown of the drink."""

        # Drink name: base price + price adjustment
        # Example:
        #   Blended drink:           $3
        #   (Since base price = $2 and blended drink charges $1 more.)
        print(
            f"{f'{self.NAME}':<{LEFT_ALIGN}}{f'${self.BASE_PRICE + self.PRICE_ADJUSTMENT:.2f}':>{RIGHT_ALIGN}}")

        # Size: price
        print(
            f"{f'  + Size {self.size}':<{LEFT_ALIGN}}{f'${self.SIZE[self.size]:.2f}':>{RIGHT_ALIGN}}")

        # Whipped cream: price (If applied)
        if self.hasWhippedCream:
            whippedCreamPrice = self.TOPPING["Whipped cream"]
            print(
                f"{f'  + Whipped cream':<{LEFT_ALIGN}}{f'${whippedCreamPrice:.2f}':>{RIGHT_ALIGN}}")

        # Milk option: price (If applied)
        if self.milkOption:
            milkOptionPrice = self.MILK_OPTION[self.milkOption]
            print(
                f"{f'  + {self.milkOption}':<{LEFT_ALIGN}}{f'${milkOptionPrice:.2f}':>{RIGHT_ALIGN}}")


class ColdDrink(Drink):
    NAME = "Cold drink"


class BlendedDrink(Drink):
    NAME = "Blended drink"
    PRICE_ADJUSTMENT = 1.0        # Blended drink is gonna charge you $1 more!


class HotDrink(Drink):
    NAME = "Hot drink"
    SIZE = {"S": 0, "M": 0.5}   # only available for size S and M
    # adding chocolate sauce to the topping
    TOPPING = {"Whipped cream": 0.5, "Chocolate Sauce": 0.5}

    def __init__(self, size: str, hasWhippedCream: bool, chocolatePumps: int = 0):
        super().__init__(size, hasWhippedCream)
        assert (0 <= chocolatePumps <=
                6), "You can only get maximum of 6 pumps of chocolate sauce."
        self.chocolatePumps = chocolatePumps

    def getChocolatePrice(self) -> float:
        """
        Calculate the price of the chocolate sauce option.
        - The first two pumps are free.
        - $0.5 for each extra pump
        """
        return max(self.chocolatePumps - 2, 0) * self.TOPPING["Chocolate Sauce"]

    def calculatePrice(self) -> float:
        """
        Add the chocolate sauce price to the total price.
        """
        return super().calculatePrice() + self.getChocolatePrice()

    def displayPriceBreakdown(self) -> None:
        super().displayPriceBreakdown()

        if self.chocolatePumps > 0:
            print(
                f"{f'  + {self.chocolatePumps} chocolate pumps':<{LEFT_ALIGN}}{f'${self.getChocolatePrice():.2f}':>{RIGHT_ALIGN}}")


class MilkTea(Drink):
    NAME = "Milk tea"
    BASE_PRICE = 2.25       # Base price is different than other drinks


class Food(Item):
    """An abstract class for breakfast item."""

    BASE_PRICE = 3.0
    TOPPING = None

    def __init__(self, topping: str = None):
        if topping:
            assert (topping in self.TOPPING), "Invalid topping"
        self.topping = topping

    def calculatePrice(self) -> float:
        """
        Add the topping price to the total price.
        """
        if self.topping:
            topping_price = self.TOPPING[self.topping]
        else:
            topping_price = 0
        return super().calculatePrice() + topping_price

    def displayPriceBreakdown(self) -> None:
        super().displayPriceBreakdown()

        if self.topping:
            print(
                f"{f'  + {self.topping}':<{LEFT_ALIGN}}{f'${self.TOPPING[self.topping]:.2f}':>{RIGHT_ALIGN}}")


class Sandwich(Food):
    NAME = "Sandwich"
    TOPPING = {"Egg": 1.0, "Turkey": 1.0}


class Bagel(Food):
    NAME = "Bagel"
    TOPPING = {"Butter": 0.5, "Cream cheese": 0.5}
