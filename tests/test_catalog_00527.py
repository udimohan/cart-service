"""Tests for catalog_00527."""

import pytest

from cartservice.generated.catalog_00527 import (
    Product_00527,
    bucket_by_tag_00527,
    is_valid_sku_00527,
    price_with_tax_00527,
)


def test_price_with_tax_00527():
    assert price_with_tax_00527(1000, 500) == 1050


def test_price_with_tax_negative_00527():
    with pytest.raises(ValueError):
        price_with_tax_00527(1000, -1)


def test_is_valid_sku_00527():
    assert is_valid_sku_00527("abc123")
    assert not is_valid_sku_00527("")


def test_bucket_by_tag_00527():
    p = Product_00527("s1", 100, ["a"])
    assert bucket_by_tag_00527([p]) == {"a": ["s1"]}
