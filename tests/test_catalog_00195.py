"""Tests for catalog_00195."""

import pytest

from cartservice.generated.catalog_00195 import (
    Product_00195,
    bucket_by_tag_00195,
    is_valid_sku_00195,
    price_with_tax_00195,
)


def test_price_with_tax_00195():
    assert price_with_tax_00195(1000, 500) == 1050


def test_price_with_tax_negative_00195():
    with pytest.raises(ValueError):
        price_with_tax_00195(1000, -1)


def test_is_valid_sku_00195():
    assert is_valid_sku_00195("abc123")
    assert not is_valid_sku_00195("")


def test_bucket_by_tag_00195():
    p = Product_00195("s1", 100, ["a"])
    assert bucket_by_tag_00195([p]) == {"a": ["s1"]}
