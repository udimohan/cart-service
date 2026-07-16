"""Tests for catalog_01091."""

import pytest

from cartservice.generated.catalog_01091 import (
    Product_01091,
    bucket_by_tag_01091,
    is_valid_sku_01091,
    price_with_tax_01091,
)


def test_price_with_tax_01091():
    assert price_with_tax_01091(1000, 500) == 1050


def test_price_with_tax_negative_01091():
    with pytest.raises(ValueError):
        price_with_tax_01091(1000, -1)


def test_is_valid_sku_01091():
    assert is_valid_sku_01091("abc123")
    assert not is_valid_sku_01091("")


def test_bucket_by_tag_01091():
    p = Product_01091("s1", 100, ["a"])
    assert bucket_by_tag_01091([p]) == {"a": ["s1"]}
