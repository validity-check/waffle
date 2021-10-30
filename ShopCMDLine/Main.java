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
        shop.add(new ShopItem("Kew Gardens 50p Brilliant Uncirculated Coin", random.nextInt(500), 1));
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
            int choice = receiveInput(sc);
            if (choice == 1) {
                printShop(shop);
            }
            if (choice == 3) {
                System.out.println("|--------------------------------|");
                System.out.println("Goodbye!");
                System.out.println("|--------------------------------|");
                System.exit(0);
                sc.close();
            }
        }
    }

    public static int receiveInput(Scanner sc) {
        int choice = 0;
        try {
            choice = sc.nextInt();
        } catch (InputMismatchException exception) {
            System.out.println("Please input a valid integer between 1 and 3.");
            sc.next();
            receiveInput(sc);
        }
        if (!(1 <= choice && 3 >= choice)) {
            System.out.println("Please input a valid integer between 1 and 3.");
            receiveInput(sc);
        }
        return choice;
    }

    public static void printShop(ArrayList<ShopItem> shop) {
        for (int i = 0; i < shop.size(); i++) {
            System.out.println("----------------------------------");
            System.out.println("ITEM " + i);
            System.out.println("NAME: " + shop.get(i).getName());
            System.out.println("PRICE: £" + shop.get(i).getPrice());
            System.out.println("STOCK: " + shop.get(i).getStock());
        }
    }

    public static void selectProduct(ArrayList<ShopItem> shop) {
        Scanner sc = new Scanner(System.in);
        System.out.println("----------------------------------");
        System.out.println("Please enter the name of the product you want to select:\n> ");
        String selection = sc.next();
        String closestName;
        int mostSimilar;
        for (int i = 0; i < shop.size(); i++) {

        }
        sc.close();
    }
}