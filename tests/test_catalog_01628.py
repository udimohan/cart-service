"""Tests for catalog_01628."""

import pytest

from cartservice.generated.catalog_01628 import (
    Product_01628,
    bucket_by_tag_01628,
    is_valid_sku_01628,
    price_with_tax_01628,
)


def test_price_with_tax_01628():
    assert price_with_tax_01628(1000, 500) == 1050


def test_price_with_tax_negative_01628():
    with pytest.raises(ValueError):
        price_with_tax_01628(1000, -1)


def test_is_valid_sku_01628():
    assert is_valid_sku_01628("abc123")
    assert not is_valid_sku_01628("")


def test_bucket_by_tag_01628():
    p = Product_01628("s1", 100, ["a"])
    assert bucket_by_tag_01628([p]) == {"a": ["s1"]}
