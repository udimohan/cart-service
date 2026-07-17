"""Tests for catalog_00161."""

import pytest

from cartservice.generated.catalog_00161 import (
    Product_00161,
    bucket_by_tag_00161,
    is_valid_sku_00161,
    price_with_tax_00161,
)


def test_price_with_tax_00161():
    assert price_with_tax_00161(1000, 500) == 1050


def test_price_with_tax_negative_00161():
    with pytest.raises(ValueError):
        price_with_tax_00161(1000, -1)


def test_is_valid_sku_00161():
    assert is_valid_sku_00161("abc123")
    assert not is_valid_sku_00161("")


def test_bucket_by_tag_00161():
    p = Product_00161("s1", 100, ["a"])
    assert bucket_by_tag_00161([p]) == {"a": ["s1"]}
