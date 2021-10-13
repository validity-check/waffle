package ShopCMDLine;

import java.util.ArrayList;
import java.util.Random;

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
        Random random = new Random();
        shop.add(new ShopItem("Hat", random.nextInt(8), random.nextInt(500)));
        shop.add(new ShopItem("Bag", random.nextInt(30), random.nextInt(90)));
        shop.add(new ShopItem("Jacket", random.nextInt(15), random.nextInt(20)));
        shop.add(new ShopItem("Kew Gardens 50p Brilliant Uncirculated Coin", random.nextInt(150), 1));
    }
}
