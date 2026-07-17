"""Tests for catalog_00269."""

import pytest

from cartservice.generated.catalog_00269 import (
    Product_00269,
    bucket_by_tag_00269,
    is_valid_sku_00269,
    price_with_tax_00269,
)


def test_price_with_tax_00269():
    assert price_with_tax_00269(1000, 500) == 1050


def test_price_with_tax_negative_00269():
    with pytest.raises(ValueError):
        price_with_tax_00269(1000, -1)


def test_is_valid_sku_00269():
    assert is_valid_sku_00269("abc123")
    assert not is_valid_sku_00269("")


def test_bucket_by_tag_00269():
    p = Product_00269("s1", 100, ["a"])
    assert bucket_by_tag_00269([p]) == {"a": ["s1"]}
