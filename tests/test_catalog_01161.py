"""Tests for catalog_01161."""

import pytest

from cartservice.generated.catalog_01161 import (
    Product_01161,
    bucket_by_tag_01161,
    is_valid_sku_01161,
    price_with_tax_01161,
)


def test_price_with_tax_01161():
    assert price_with_tax_01161(1000, 500) == 1050


def test_price_with_tax_negative_01161():
    with pytest.raises(ValueError):
        price_with_tax_01161(1000, -1)


def test_is_valid_sku_01161():
    assert is_valid_sku_01161("abc123")
    assert not is_valid_sku_01161("")


def test_bucket_by_tag_01161():
    p = Product_01161("s1", 100, ["a"])
    assert bucket_by_tag_01161([p]) == {"a": ["s1"]}
