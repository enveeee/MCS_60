// Component Interface
interface Car {
    void assemble();
}

// Concrete Component
class BasicCar implements Car {
    public void assemble() {
        System.out.print("Basic Car");
    }
}

// Decorator
class CarDecorator implements Car {
    protected Car decoratedCar;

    public CarDecorator(Car c) {
        this.decoratedCar = c;
    }

    public void assemble() {
        this.decoratedCar.assemble();
    }
}

// Concrete Decorators
class SportsCar extends CarDecorator {
    public SportsCar(Car c) {
        super(c);
    }

    public void assemble() {
        super.assemble();
        System.out.print(" + Sports Car features");
    }
}

class LuxuryCar extends CarDecorator {
    public LuxuryCar(Car c) {
        super(c);
    }

    public void assemble() {
        super.assemble();
        System.out.print(" + Luxury Car features");
    }
}

public class Main {
    public static void main(String[] args) {
        Car s1 = new SportsCar(new BasicCar());
        System.out.print("Sports Car: ");
        s1.assemble();

        System.out.println();

        Car s2 = new LuxuryCar(new BasicCar());
        System.out.print("Luxury Car: ");
        s2.assemble();

        System.out.println();

        Car s = new SportsCar(new LuxuryCar(new BasicCar()));
        System.out.print("Sports + Luxury Car: ");
        s.assemble();
    }
}

