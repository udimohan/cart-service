"""Tests for catalog_00192."""

import pytest

from cartservice.generated.catalog_00192 import (
    Product_00192,
    bucket_by_tag_00192,
    is_valid_sku_00192,
    price_with_tax_00192,
)


def test_price_with_tax_00192():
    assert price_with_tax_00192(1000, 500) == 1050


def test_price_with_tax_negative_00192():
    with pytest.raises(ValueError):
        price_with_tax_00192(1000, -1)


def test_is_valid_sku_00192():
    assert is_valid_sku_00192("abc123")
    assert not is_valid_sku_00192("")


def test_bucket_by_tag_00192():
    p = Product_00192("s1", 100, ["a"])
    assert bucket_by_tag_00192([p]) == {"a": ["s1"]}
