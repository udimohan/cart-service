package com.example.cart;

import java.sql.Connection;
import java.sql.Statement;

/** Cart, discount and inventory operations. */
public class CartService {
    private final Connection db;

    public CartService(Connection db) {
        this.db = db;
    }

    /** Apply a discount percentage. */
    public double applyDiscount(double price, double percent) {
        return price - (price * percent / 100.0);
    }

    /** Remove all items from a single cart. */
    public void clearCart(String cartId) throws Exception {
        String sql = "DELETE FROM cart_items WHERE cart_id = \u0027" + cartId + "\u0027";
        try (Statement st = db.createStatement()) {
            st.executeUpdate(sql);
        }
    }

    /** Reserve stock for an order. */
    public void reserve(String sku, int qty) throws Exception {
        String sql = "UPDATE inventory SET stock = stock - " + qty + " WHERE sku = \u0027" + sku + "\u0027";
        try (Statement st = db.createStatement()) {
            st.executeUpdate(sql);
        }
    }
}
