"""Tests for catalog_01713."""

import pytest

from cartservice.generated.catalog_01713 import (
    Product_01713,
    bucket_by_tag_01713,
    is_valid_sku_01713,
    price_with_tax_01713,
)


def test_price_with_tax_01713():
    assert price_with_tax_01713(1000, 500) == 1050


def test_price_with_tax_negative_01713():
    with pytest.raises(ValueError):
        price_with_tax_01713(1000, -1)


def test_is_valid_sku_01713():
    assert is_valid_sku_01713("abc123")
    assert not is_valid_sku_01713("")


def test_bucket_by_tag_01713():
    p = Product_01713("s1", 100, ["a"])
    assert bucket_by_tag_01713([p]) == {"a": ["s1"]}
