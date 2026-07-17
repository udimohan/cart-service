"""Tests for catalog_00713."""

import pytest

from cartservice.generated.catalog_00713 import (
    Product_00713,
    bucket_by_tag_00713,
    is_valid_sku_00713,
    price_with_tax_00713,
)


def test_price_with_tax_00713():
    assert price_with_tax_00713(1000, 500) == 1050


def test_price_with_tax_negative_00713():
    with pytest.raises(ValueError):
        price_with_tax_00713(1000, -1)


def test_is_valid_sku_00713():
    assert is_valid_sku_00713("abc123")
    assert not is_valid_sku_00713("")


def test_bucket_by_tag_00713():
    p = Product_00713("s1", 100, ["a"])
    assert bucket_by_tag_00713([p]) == {"a": ["s1"]}
