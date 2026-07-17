"""Tests for catalog_00350."""

import pytest

from cartservice.generated.catalog_00350 import (
    Product_00350,
    bucket_by_tag_00350,
    is_valid_sku_00350,
    price_with_tax_00350,
)


def test_price_with_tax_00350():
    assert price_with_tax_00350(1000, 500) == 1050


def test_price_with_tax_negative_00350():
    with pytest.raises(ValueError):
        price_with_tax_00350(1000, -1)


def test_is_valid_sku_00350():
    assert is_valid_sku_00350("abc123")
    assert not is_valid_sku_00350("")


def test_bucket_by_tag_00350():
    p = Product_00350("s1", 100, ["a"])
    assert bucket_by_tag_00350([p]) == {"a": ["s1"]}
