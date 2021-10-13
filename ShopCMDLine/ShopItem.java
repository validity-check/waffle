package ShopCMDLine;

public class ShopItem {
    private String name;
    private double price;
    private int stock;

    public ShopItem(String name, double price, int stock) {
        this.name = name;
        this.price = price;
        this.stock = stock;
    }

    public String getName() {
        return this.name;
    }

    public double getPrice() {
        return this.price;
    }

    public int getStock() {
        return this.stock;
    }

    public void stockUp(int increment) {
        this.stock += increment;
    }

    public void stockDown(int decrement) {
        this.stock -= decrement;
    }
}
