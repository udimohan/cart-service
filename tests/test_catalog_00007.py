"""Tests for catalog_00007."""

import pytest

from cartservice.generated.catalog_00007 import (
    Product_00007,
    bucket_by_tag_00007,
    is_valid_sku_00007,
    price_with_tax_00007,
)


def test_price_with_tax_00007():
    assert price_with_tax_00007(1000, 500) == 1050


def test_price_with_tax_negative_00007():
    with pytest.raises(ValueError):
        price_with_tax_00007(1000, -1)


def test_is_valid_sku_00007():
    assert is_valid_sku_00007("abc123")
    assert not is_valid_sku_00007("")


def test_bucket_by_tag_00007():
    p = Product_00007("s1", 100, ["a"])
    assert bucket_by_tag_00007([p]) == {"a": ["s1"]}
