"""Tests for catalog_00650."""

import pytest

from cartservice.generated.catalog_00650 import (
    Product_00650,
    bucket_by_tag_00650,
    is_valid_sku_00650,
    price_with_tax_00650,
)


def test_price_with_tax_00650():
    assert price_with_tax_00650(1000, 500) == 1050


def test_price_with_tax_negative_00650():
    with pytest.raises(ValueError):
        price_with_tax_00650(1000, -1)


def test_is_valid_sku_00650():
    assert is_valid_sku_00650("abc123")
    assert not is_valid_sku_00650("")


def test_bucket_by_tag_00650():
    p = Product_00650("s1", 100, ["a"])
    assert bucket_by_tag_00650([p]) == {"a": ["s1"]}
