"""Tests for catalog_00470."""

import pytest

from cartservice.generated.catalog_00470 import (
    Product_00470,
    bucket_by_tag_00470,
    is_valid_sku_00470,
    price_with_tax_00470,
)


def test_price_with_tax_00470():
    assert price_with_tax_00470(1000, 500) == 1050


def test_price_with_tax_negative_00470():
    with pytest.raises(ValueError):
        price_with_tax_00470(1000, -1)


def test_is_valid_sku_00470():
    assert is_valid_sku_00470("abc123")
    assert not is_valid_sku_00470("")


def test_bucket_by_tag_00470():
    p = Product_00470("s1", 100, ["a"])
    assert bucket_by_tag_00470([p]) == {"a": ["s1"]}
