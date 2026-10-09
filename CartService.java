package com.example.cart;

import java.sql.Connection;
import java.sql.PreparedStatement;

/** Cart, discount and inventory operations. */
public class CartService {
    private final Connection db;

    public CartService(Connection db) {
        this.db = db;
    }

    /** Apply a discount percentage, clamped to [0, 100]. */
    public double applyDiscount(double price, double percent) {
        double p = Math.max(0, Math.min(percent, 100));
        return price - (price * p / 100.0);
    }

    /** Remove all items from a single cart. */
    public void clearCart(String cartId) throws Exception {
        if (cartId == null || cartId.isBlank()) {
            throw new IllegalArgumentException("cartId is required");
        }
        try (PreparedStatement st = db.prepareStatement(
                "DELETE FROM cart_items WHERE cart_id = ?")) {
            st.setString(1, cartId);
            st.executeUpdate();
        }
    }

    /** Reserve stock, refusing to oversell. */
    public void reserve(String sku, int qty) throws Exception {
        try (PreparedStatement st = db.prepareStatement(
                "UPDATE inventory SET stock = stock - ? WHERE sku = ? AND stock >= ?")) {
            st.setInt(1, qty);
            st.setString(2, sku);
            st.setInt(3, qty);
            int updated = st.executeUpdate();
            if (updated == 0) {
                throw new IllegalStateException("insufficient stock for " + sku);
            }
        }
    }
}
