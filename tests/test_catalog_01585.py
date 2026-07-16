"""Tests for catalog_01585."""

import pytest

from cartservice.generated.catalog_01585 import (
    Product_01585,
    bucket_by_tag_01585,
    is_valid_sku_01585,
    price_with_tax_01585,
)


def test_price_with_tax_01585():
    assert price_with_tax_01585(1000, 500) == 1050


def test_price_with_tax_negative_01585():
    with pytest.raises(ValueError):
        price_with_tax_01585(1000, -1)


def test_is_valid_sku_01585():
    assert is_valid_sku_01585("abc123")
    assert not is_valid_sku_01585("")


def test_bucket_by_tag_01585():
    p = Product_01585("s1", 100, ["a"])
    assert bucket_by_tag_01585([p]) == {"a": ["s1"]}
