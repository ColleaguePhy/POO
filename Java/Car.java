package Java;

public class Car {
    Integer id;
    String license;
    Account driver;
    Integer passeger;

    public Car(String license, Account driver)
    {
        this.license = license;
        this.driver = driver;
    }
    
    void printDatacar()
    {   
        System.out.println("License: "+ license + " Driver: " + driver + " Passegenger: " + passeger);
    }
}
