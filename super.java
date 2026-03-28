// Parent class
class Animal {
    String color = "White";

    // Parent constructor
    Animal() {
        System.out.println("Animal constructor called");
    }

    void eat() {
        System.out.println("Animal is eating");
    }
}

// Child class
class Dog extends Animal {
    String color = "Black";

    // Child constructor
    Dog() {
        super(); // calls parent constructor
        System.out.println("Dog constructor called");
    }

    void showColor() {
        System.out.println("Dog color: " + color);
        System.out.println("Animal color: " + super.color); // accessing parent variable
    }

    void eat() {
        super.eat(); // calling parent method
        System.out.println("Dog is eating");
    }
}

// Main class
public class Main {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.showColor();
        d.eat();
    }
}
