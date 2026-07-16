"""Tests for catalog_01269."""

import pytest

from cartservice.generated.catalog_01269 import (
    Product_01269,
    bucket_by_tag_01269,
    is_valid_sku_01269,
    price_with_tax_01269,
)


def test_price_with_tax_01269():
    assert price_with_tax_01269(1000, 500) == 1050


def test_price_with_tax_negative_01269():
    with pytest.raises(ValueError):
        price_with_tax_01269(1000, -1)


def test_is_valid_sku_01269():
    assert is_valid_sku_01269("abc123")
    assert not is_valid_sku_01269("")


def test_bucket_by_tag_01269():
    p = Product_01269("s1", 100, ["a"])
    assert bucket_by_tag_01269([p]) == {"a": ["s1"]}
