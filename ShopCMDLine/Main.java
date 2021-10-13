package ShopCMDLine;

import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Random;
import java.util.Scanner;

/**
 * Main
 */
public class Main {

    public static void main(String[] args) {
        System.out.println(
                "Welcome to ShopCMDLine, a shop built onto your command prompt because we like to be confusing, and really can't be bothered to make a website.");
        ArrayList<ShopItem> Shop = new ArrayList<ShopItem>();
        createShop(Shop);
        shopLoop(Shop);
    }

    public static void createShop(ArrayList<ShopItem> shop) {
        Random random = new Random();
        shop.add(new ShopItem("Hat", random.nextInt(8), random.nextInt(500)));
        shop.add(new ShopItem("Bag", random.nextInt(30), random.nextInt(90)));
        shop.add(new ShopItem("Jacket", random.nextInt(15), random.nextInt(20)));
        shop.add(new ShopItem("Kew Gardens 50p Brilliant Uncirculated Coin", random.nextInt(150), 1));
    }

    public static void shopLoop(ArrayList<ShopItem> shop) {
        while (true) {
            Scanner sc = new Scanner(System.in);
            System.out.println("|--------------------------------|");
            System.out.println("Select your option");
            System.out.println("|--------------------------------|");
            System.out.println("1 - Print all shop products, their costs and stocks.");
            System.out.println("2 - Select a product by name");
            System.out.println("3 - Exit");
            int choice = 0;
            boolean valid = false;
            while (!valid) {
                try {
                    choice = sc.nextInt();
                    if (1 <= choice && choice >= 3) {
                        valid = true;
                        sc.next();
                    } else {
                        System.out.println("Please make sure you put an integer between one and three.");
                        sc.next();
                    }
                } catch (InputMismatchException exception) {
                    System.out.println("Please make sure you put an integer between one and three.");
                    sc.next();
                }
            }
            if (choice == 3) {
                System.out.println("|--------------------------------|");
                System.out.println("Goodbye!");
                System.out.println("|--------------------------------|");
                System.exit(0);
                sc.close();
            }
            sc.close();
        }
    }
}
