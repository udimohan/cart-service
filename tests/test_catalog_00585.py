"""Tests for catalog_00585."""

import pytest

from cartservice.generated.catalog_00585 import (
    Product_00585,
    bucket_by_tag_00585,
    is_valid_sku_00585,
    price_with_tax_00585,
)


def test_price_with_tax_00585():
    assert price_with_tax_00585(1000, 500) == 1050


def test_price_with_tax_negative_00585():
    with pytest.raises(ValueError):
        price_with_tax_00585(1000, -1)


def test_is_valid_sku_00585():
    assert is_valid_sku_00585("abc123")
    assert not is_valid_sku_00585("")


def test_bucket_by_tag_00585():
    p = Product_00585("s1", 100, ["a"])
    assert bucket_by_tag_00585([p]) == {"a": ["s1"]}
