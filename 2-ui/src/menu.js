class Drink {
    static basePrice = 2.0;
    static size = {
        name: "size",
        select: { s: 0.0, m: 0.5, l: 1.0, xl: 1.5 }
    };
    static whippedCream = {
        name: "whippedCream",
        select: { no: 0.0, yes: 0.5 }
    };
    static milkOption = {
        name: "milkOption",
        select: { no: 0.0, wholeMilk: 0.0, almondMilk: 0.5 }
    };

    getOptions() {
        return [
            {...this.constructor.size},
            {...this.constructor.whippedCream},
            {...this.constructor.milkOption}
        ]
    }
}

class ColdDrink extends Drink {
    static name = "coldDrink";
}

class BlendedDrink extends Drink {
    static name = "blendedDrink"
    static basePrice = 3.0;
}

class HotDrink extends Drink {
    static name = "hotDrink"
    static size = {
        name: "size",
        select: { s: 0.0, m: 0.5 }
    };
    static chocolateSauce = {
        name: "chocolateSauce",
        select: {'0p': 0.0, '1p': 0.0, '2p': 0.0, '3p':0.5, '4p':1.0, '5p':1.5, '6p':2.0}
    }
    getOptions() {
        return [...super.getOptions(), {...this.constructor.chocolateSauce}]
    }
}

class MilkTea extends Drink {
    static name = "milkTea"
    static basePrice = 2.25
    
}

class Food {
    static basePrice = 3.0;
    static topping = {
        name: "topping",
        select: {}
    }

    getOptions() {
        return [
            {...this.constructor.topping}
        ]
    }
}

class Sandwich extends Food {
    static name = "sandwich"
    static topping = {
        name: "topping",
        select: {no: 0.0, egg: 1.0, turkey: 1.0}
    }
}

class Bagel extends Food {
    static name = "bagel"
    static topping = {
        name: "topping",
        select: {no: 0.0, butter: 0.5, creamCheese: 0.5}
    }
}

const MENU = [HotDrink, ColdDrink, BlendedDrink, MilkTea, Sandwich, Bagel]

export default MENU;