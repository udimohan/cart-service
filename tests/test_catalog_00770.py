"""Tests for catalog_00770."""

import pytest

from cartservice.generated.catalog_00770 import (
    Product_00770,
    bucket_by_tag_00770,
    is_valid_sku_00770,
    price_with_tax_00770,
)


def test_price_with_tax_00770():
    assert price_with_tax_00770(1000, 500) == 1050


def test_price_with_tax_negative_00770():
    with pytest.raises(ValueError):
        price_with_tax_00770(1000, -1)


def test_is_valid_sku_00770():
    assert is_valid_sku_00770("abc123")
    assert not is_valid_sku_00770("")


def test_bucket_by_tag_00770():
    p = Product_00770("s1", 100, ["a"])
    assert bucket_by_tag_00770([p]) == {"a": ["s1"]}
