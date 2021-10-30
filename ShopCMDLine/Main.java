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
        shop.add(new ShopItem("Kew Gardens 50p", random.nextInt(500), 1));
    }

    public static void shopLoop(ArrayList<ShopItem> shop) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("|--------------------------------|");
            System.out.println("Select your option");
            System.out.println("|--------------------------------|");
            System.out.println("1 - Print all shop products, their costs and stocks.");
            System.out.println("2 - Select a product by name");
            System.out.println("3 - Exit");
            int choice = receiveInput(sc, 1, 3);
            if (choice == 1) {
                printShop(shop);
            }
            if (choice == 2) {
                selectProduct(shop, sc);
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

    public static int receiveInput(Scanner sc, int low, int high) {
        int choice = 0;
        try {
            choice = sc.nextInt();
        } catch (InputMismatchException exception) {
            System.out.println("Please input a valid integer between " + low + " and " + high + ".");
            sc.next();
            receiveInput(sc, low, high);
        }
        if (!(1 <= choice && 3 >= choice)) {
            System.out.println("Please input a valid integer between " + low + " and " + high + ".");
            receiveInput(sc, low, high);
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

    public static void selectProduct(ArrayList<ShopItem> shop, Scanner sc) {
        System.out.println("----------------------------------");
        System.out.println("Please enter the name of the product you want to select:\n> ");
        String selection = sc.next();
        int closestName = 0;
        double mostSimilar = 0;
        for (int i = 0; i < shop.size(); i++) {
            String currItem = shop.get(i).getName().toLowerCase();
            String longer = currItem, shorter = selection;
            if (selection.length() > currItem.length()) {
                longer = selection;
                shorter = currItem;
            }
            double matchingChar = (longer.length() - editDistance(longer, shorter)) / (double) longer.length();
            if (matchingChar > mostSimilar) {
                mostSimilar = matchingChar;
                closestName = i;
            }
        }
        System.out.println("Did you mean " + shop.get(closestName).getName() + "?" + mostSimilar + " " + closestName);
        System.out.println("Y to confirm, N for no");
        String confirmation = "";
        boolean yn = true;
        while (yn) {
            confirmation = sc.nextLine().toLowerCase();
            switch (confirmation) {
            case "y":
                System.out.println("Product details:");
                System.out.println("----------------------------------");
                System.out.println("ITEM " + closestName);
                System.out.println("NAME: " + shop.get(closestName).getName());
                System.out.println("PRICE: £" + shop.get(closestName).getPrice());
                System.out.println("STOCK: " + shop.get(closestName).getStock());
                System.out.println("----------------------------------");
                System.out.println("What would you like to do with this product?");
                System.out.println("1 - Buy product.");
                System.out.println("2 - Stock up on product.");
                System.out.println("3 - Go back");
                int choice = receiveInput(sc, 1, 3);
                if (choice == 1) {
                    if (shop.get(closestName).getStock() == 0) {
                        System.out.println("Sorry, this item is out of stock");
                        return;
                    }
                    System.out.println("How many do you want?");
                    int qty = receiveInput(sc, 1, shop.get(closestName).getStock());
                    shop.get(closestName).stockDown(qty);

                }
            case "n":
                yn = false;
            }
        }
    }

    public static int editDistance(String s1, String s2) {
        s1 = s1.toLowerCase();
        s2 = s2.toLowerCase();

        int[] costs = new int[s2.length() + 1];
        for (int i = 0; i <= s1.length(); i++) {
            int lastValue = i;
            for (int j = 0; j <= s2.length(); j++) {
                if (i == 0)
                    costs[j] = j;
                else {
                    if (j > 0) {
                        int newValue = costs[j - 1];
                        if (s1.charAt(i - 1) != s2.charAt(j - 1))
                            newValue = Math.min(Math.min(newValue, lastValue), costs[j]) + 1;
                        costs[j - 1] = lastValue;
                        lastValue = newValue;
                    }
                }
            }
            if (i > 0)
                costs[s2.length()] = lastValue;
        }
        return costs[s2.length()];
    }
}
