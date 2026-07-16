"""Tests for catalog_00372."""

import pytest

from cartservice.generated.catalog_00372 import (
    Product_00372,
    bucket_by_tag_00372,
    is_valid_sku_00372,
    price_with_tax_00372,
)


def test_price_with_tax_00372():
    assert price_with_tax_00372(1000, 500) == 1050


def test_price_with_tax_negative_00372():
    with pytest.raises(ValueError):
        price_with_tax_00372(1000, -1)


def test_is_valid_sku_00372():
    assert is_valid_sku_00372("abc123")
    assert not is_valid_sku_00372("")


def test_bucket_by_tag_00372():
    p = Product_00372("s1", 100, ["a"])
    assert bucket_by_tag_00372([p]) == {"a": ["s1"]}
