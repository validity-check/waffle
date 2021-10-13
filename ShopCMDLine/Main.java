package ShopCMDLine;

import java.util.ArrayList;

/**
 * Main
 */
public class Main {

    public static void main(String[] args) {
        System.out.println(
                "Welcome to ShopCMDLine, a shop built onto your command prompt because we like to be confusing, and really can't be bothered to make a website.");
        ArrayList<ShopItem> Shop = new ArrayList<ShopItem>();
        createShop(Shop);
    }

    public static void createShop(ArrayList<ShopItem> shop) {
        shop.add(new ShopItem("Hat", 3, 94));
        shop.add(new ShopItem("Bag", 12, 20));
        shop.add(new ShopItem("Jacket", 30, 77));
        shop.add(new ShopItem("Kew Gardens 50p Brilliant Uncirculated Coin", 1, 125));
    }
}
