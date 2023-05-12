from typing import List
from coffee import Item, HotDrink, ColdDrink, BlendedDrink, MilkTea, Sandwich, Bagel, LEFT_ALIGN, RIGHT_ALIGN

BREAKLINE = "-" * 58    # a break line in the printed bill

DRINK = {
    "hot": HotDrink,
    "cold": ColdDrink,
    "blended": BlendedDrink,
    "milk tea": MilkTea
}

FOOD = {
    "sandwich": Sandwich,
    "bagel": Bagel
}


def calculatePrice1(drinkType: str, size: str, hasWhippedCream: bool) -> float:
    """
    Calculate the price of a coffee order based on the following parameters:
    @param drinkType: hot, cold, or blended
    @param size: S, M, or L
    @param hasWhippedCream: True or False (with or without)
    @return: Total price of the coffee order

    >>> calculatePrice1("hot", "s", False)
    2.0
    >>> calculatePrice1("hot", "m", False)
    2.5
    >>> calculatePrice1("hot", "s", True)
    2.5
    >>> calculatePrice1("hot", "m", True)
    3.0
    >>> calculatePrice1("cold", "s", False)
    2.0
    >>> calculatePrice1("cold", "m", False)
    2.5
    >>> calculatePrice1("cold", "l", False)
    3.0
    >>> calculatePrice1("cold", "s", True)
    2.5
    >>> calculatePrice1("cold", "m", True)
    3.0
    >>> calculatePrice1("cold", "l", True)
    3.5
    >>> calculatePrice1("blended", "s", False)
    3.0
    >>> calculatePrice1("blended", "m", False)
    3.5
    >>> calculatePrice1("blended", "l", False)
    4.0
    >>> calculatePrice1("blended", "s", True)
    3.5
    >>> calculatePrice1("blended", "m", True)
    4.0
    >>> calculatePrice1("blended", "l", True)
    4.5
    """
    assert (drinkType in DRINK), "Invalid drink type."
    return DRINK[drinkType](size, hasWhippedCream).calculatePrice()


def calculatePrice2(drinkType: str, size: str, hasWhippedCream: bool, milkOption: str) -> float:
    """
    Calculate the price of a coffee order based on the following parameters:
    @param drinkType: hot, cold, or blended
    @param size: S, M, or L
    @param hasWhippedCream: True or False (with or without)
    @param milkOption: whole milk or almond milk
    @return: Total price of the coffee order

    >>> calculatePrice2("milk tea", "s", False, "whole milk")
    2.25
    >>> calculatePrice2("milk tea", "s", False, "almond milk")
    2.75
    >>> calculatePrice2("milk tea", "m", False, "whole milk")
    2.75
    >>> calculatePrice2("milk tea", "m", False, "almond milk")
    3.25
    >>> calculatePrice2("milk tea", "l", False, "whole milk")
    3.25
    >>> calculatePrice2("milk tea", "l", False, "almond milk")
    3.75
    >>> calculatePrice2("milk tea", "xl", False, "whole milk")
    3.75
    >>> calculatePrice2("milk tea", "xl", False, "almond milk")
    4.25
    >>> calculatePrice2("milk tea", "s", True, "whole milk")
    2.75
    >>> calculatePrice2("milk tea", "s", True, "almond milk")
    3.25
    >>> calculatePrice2("milk tea", "m", True, "whole milk")
    3.25
    >>> calculatePrice2("milk tea", "m", True, "almond milk")
    3.75
    >>> calculatePrice2("milk tea", "l", True, "whole milk")
    3.75
    >>> calculatePrice2("milk tea", "l", True, "almond milk")
    4.25
    >>> calculatePrice2("milk tea", "xl", True, "whole milk")
    4.25
    >>> calculatePrice2("milk tea", "xl", True, "almond milk")
    4.75
    >>> calculatePrice2("blended", "xl", True, "almond milk")
    5.5
    >>> calculatePrice2("blended", "xl", True, "whole milk")
    5.0
    """
    assert (drinkType in DRINK), "Invalid drink type."
    return DRINK[drinkType](size, hasWhippedCream, milkOption.capitalize()).calculatePrice()


def calculatePrice3(drinkType: str, size: str, hasWhippedCream: bool, milkOption: str, chocolatePumps: int) -> float:
    """
    Calculate the price of a coffee order based on the following parameters:
    @param drinkType: hot, cold, or blended
    @param size: S, M, or L
    @param hasWhippedCream: True or False (with or without)
    @param milkOption: whole milk or almond milk
    @param chocolatePumps: # pumps of chocolate sauce (only applied for hot drinks and you can only get maximum of 6 pumps)
    @return: Total price of the coffee order

    >>> calculatePrice3("hot", "s", False, None, 2)
    2.0
    >>> calculatePrice3("hot", "s", False, None, 4)
    3.0
    >>> calculatePrice3("hot", "s", False, None, 6)
    4.0
    >>> calculatePrice3("hot", "m", True, None, 6)
    5.0
    """
    assert (drinkType in DRINK), "Invalid drink type."
    if drinkType == "hot":
        return HotDrink(size, hasWhippedCream, milkOption, chocolatePumps).calculatePrice()
    return calculatePrice2(drinkType, size, hasWhippedCream, milkOption)


def calculatePrice4(breakfastItem: str, topping: str) -> float:
    """
    Calculate the price of a breakfast order based on the following parameters:
    @param breakfastItem: sandwich or bagel
    @param topping: egg or turkey for sandwich, butter or cream cheese for bagel
    @return: Total price of the breakfast order

    >>> calculatePrice4("sandwich", None) 
    3.0
    >>> calculatePrice4("sandwich", "Egg") 
    4.0
    >>> calculatePrice4("sandwich", "Turkey") 
    4.0
    >>> calculatePrice4("bagel", None) 
    3.0
    >>> calculatePrice4("bagel", "Butter") 
    3.5
    >>> calculatePrice4("bagel", "Cream cheese") 
    3.5
    """
    assert (breakfastItem in FOOD), "Invalid breakfast item."
    return FOOD[breakfastItem](topping).calculatePrice()


def calculatePrice5(items: List[Item], tax_rate: float) -> float:
    """
    Calculate the price of a list of items and print out the bill with the breakdown price for each item in a pretty format.
    @param items: List of items
    @param tax_rate: vat
    @return: Total price of all the items in the list
    """
    print("Order")
    print(BREAKLINE)
    subtotal = 0    # the subtotal value without vat
    order = 1       # keep track the order of items in the bill

    # Loop through each item in the list, add the price to the subtotal
    # and print out the price breakdown to the console
    for item in items:
        print(f"#{order}")
        order += 1
        subtotal += item.calculatePrice()
        item.displayPriceBreakdown()
        print(BREAKLINE)

    # Footer of the bill including tax rate and total price
    vat = subtotal * tax_rate / 100
    total = subtotal + vat
    print(f"{'Subtotal without VAT':<{LEFT_ALIGN}}{f'${subtotal:.2f}':>{RIGHT_ALIGN}}")
    print(f"{f'VAT {tax_rate:.2f}% of ${subtotal:.2f}':<{LEFT_ALIGN}}{f'${vat:.2f}':>{RIGHT_ALIGN}}")
    print(f"{'Total':<{LEFT_ALIGN}}{f'${total:.2f}':>{RIGHT_ALIGN}}")

    return total


if __name__ == "__main__":
    items = [
        HotDrink('s', False, None, 2),
        HotDrink('m', True, None, 6),
        ColdDrink('xl', False, "Whole milk"),
        BlendedDrink('xl', False),
        MilkTea('xl', True, "Almond milk"),
        Sandwich("Egg"),
        Sandwich(None),
        Bagel("Cream cheese"),
        BlendedDrink('xl', True, "Almond milk")
    ]
    calculatePrice5(items, 7.25)
