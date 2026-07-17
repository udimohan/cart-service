"""Tests for catalog_00900."""

import pytest

from cartservice.generated.catalog_00900 import (
    Product_00900,
    bucket_by_tag_00900,
    is_valid_sku_00900,
    price_with_tax_00900,
)


def test_price_with_tax_00900():
    assert price_with_tax_00900(1000, 500) == 1050


def test_price_with_tax_negative_00900():
    with pytest.raises(ValueError):
        price_with_tax_00900(1000, -1)


def test_is_valid_sku_00900():
    assert is_valid_sku_00900("abc123")
    assert not is_valid_sku_00900("")


def test_bucket_by_tag_00900():
    p = Product_00900("s1", 100, ["a"])
    assert bucket_by_tag_00900([p]) == {"a": ["s1"]}
