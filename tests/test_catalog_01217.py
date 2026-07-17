"""Tests for catalog_01217."""

import pytest

from cartservice.generated.catalog_01217 import (
    Product_01217,
    bucket_by_tag_01217,
    is_valid_sku_01217,
    price_with_tax_01217,
)


def test_price_with_tax_01217():
    assert price_with_tax_01217(1000, 500) == 1050


def test_price_with_tax_negative_01217():
    with pytest.raises(ValueError):
        price_with_tax_01217(1000, -1)


def test_is_valid_sku_01217():
    assert is_valid_sku_01217("abc123")
    assert not is_valid_sku_01217("")


def test_bucket_by_tag_01217():
    p = Product_01217("s1", 100, ["a"])
    assert bucket_by_tag_01217([p]) == {"a": ["s1"]}
