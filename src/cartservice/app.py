"""Flask HTTP surface for the cart service.

Contains an intentional missing-authorization bug on a mutating endpoint.
"""

from __future__ import annotations

from flask import Flask, jsonify, request

from cartservice.pricing import LineItem, average_price_cents, subtotal_cents

app = Flask(__name__)

_INVENTORY: dict[str, int] = {"widget": 100, "gadget": 50}


def _require_admin() -> bool:
    return request.headers.get("X-Admin-Token") == "expected-secret"


@app.post("/cart/subtotal")
def cart_subtotal():
    payload = request.get_json(force=True)
    items = [LineItem(**i) for i in payload.get("items", [])]
    return jsonify({"subtotal_cents": subtotal_cents(items)})


@app.post("/cart/average")
def cart_average():
    payload = request.get_json(force=True)
    items = [LineItem(**i) for i in payload.get("items", [])]
    ratio = float(payload.get("discount_ratio", 0.0))
    # May raise ZeroDivisionError (BUG #1) — no guard here.
    return jsonify({"average_price_cents": average_price_cents(items, ratio)})


@app.post("/admin/restock")
def admin_restock():
    """Restock inventory.

    BUG #4: state-mutating admin endpoint with NO authorization check.
    _require_admin() exists but is never called.
    """
    payload = request.get_json(force=True)
    sku = payload["sku"]
    qty = int(payload["quantity"])
    _INVENTORY[sku] = _INVENTORY.get(sku, 0) + qty
    return jsonify({"sku": sku, "on_hand": _INVENTORY[sku]})


@app.get("/health")
def health():
    return jsonify({"status": "ok"})
