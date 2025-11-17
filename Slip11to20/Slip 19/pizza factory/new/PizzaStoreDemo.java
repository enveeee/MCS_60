
abstract class Pizza {

    String name;
    String dough;
    String sauce;

    public void prepare() {
        System.out.println("\n\nPreparing: " + name);
        System.out.println("Tossing dough: " + dough);
        System.out.println("Adding sauce: " + sauce);
    }

    public void bake() {
        System.out.println("Baking " + name);
    }

    public void cut() {
        System.out.println("Cutting " + name);
    }

    public void box() {
        System.out.println("Boxing " + name);
    }
}

class NyStyleCheesePizza extends Pizza {
    public NyStyleCheesePizza() {
        name = "New York Style Cheeze Pizza";
        dough = "Thin Crust Dough";
        sauce = "Marinara Sauce";
    }
}

class ChicagoStyleCheesePizza extends Pizza {
    public ChicagoStyleCheesePizza() {
        name = "Chicago Style Cheese Pizza";
        dough = "Thick Crust Dough";
        sauce = "Plum Tomato Sauce";
    }

    @Override
    public void cut() {
        System.out.println("Cutting the pizza into square slices");
    }
}

abstract class PizzaStore {
    public abstract Pizza createPizza(String type);

    public Pizza orderPizza(String type) {
        Pizza pizza = createPizza(type);
        pizza.prepare();
        pizza.bake();
        pizza.cut();
        pizza.box();
        return pizza;
    }
}

class NyPizzaStore extends PizzaStore {
    public Pizza createPizza(String type) {
        if (type.equals("cheese")) {
            return new NyStyleCheesePizza();
        }
        return null;
    }
}

class ChicagoPizzaStore extends PizzaStore {
    public Pizza createPizza(String type) {
        if (type.equals("cheese")) {
            return new ChicagoStyleCheesePizza();
        }
        return null;
    }
}

public class PizzaStoreDemo {
    public static void main(String[] args) {
        PizzaStore nyStore = new NyPizzaStore();
        PizzaStore chicagoStore = new ChicagoPizzaStore();

        nyStore.orderPizza("cheese");
        chicagoStore.orderPizza("cheese");

        System.out.println("\n\n");
    }
}
