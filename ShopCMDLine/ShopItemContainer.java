package ShopCMDLine;

import java.util.ArrayList;

public class ShopItemContainer {
    private ArrayList<ShopItem> items;

    public ShopItemContainer(ArrayList<ShopItem> items) {
        this.items = items;
    }

    public ArrayList<ShopItem> getItems() {
        return this.items;
    }
}
