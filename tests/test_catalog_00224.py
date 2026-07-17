"""Tests for catalog_00224."""

import pytest

from cartservice.generated.catalog_00224 import (
    Product_00224,
    bucket_by_tag_00224,
    is_valid_sku_00224,
    price_with_tax_00224,
)


def test_price_with_tax_00224():
    assert price_with_tax_00224(1000, 500) == 1050


def test_price_with_tax_negative_00224():
    with pytest.raises(ValueError):
        price_with_tax_00224(1000, -1)


def test_is_valid_sku_00224():
    assert is_valid_sku_00224("abc123")
    assert not is_valid_sku_00224("")


def test_bucket_by_tag_00224():
    p = Product_00224("s1", 100, ["a"])
    assert bucket_by_tag_00224([p]) == {"a": ["s1"]}
