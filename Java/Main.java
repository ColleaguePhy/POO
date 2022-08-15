package Java;

class Main {
    public static void main(String[] args) {
        System.out.println("Hola mundo");
        Car car = new Car("AMG123",new Account("Andres Herrera", "AND12"));
        car.printDatacar();
    }
}