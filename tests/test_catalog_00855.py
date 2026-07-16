"""Tests for catalog_00855."""

import pytest

from cartservice.generated.catalog_00855 import (
    Product_00855,
    bucket_by_tag_00855,
    is_valid_sku_00855,
    price_with_tax_00855,
)


def test_price_with_tax_00855():
    assert price_with_tax_00855(1000, 500) == 1050


def test_price_with_tax_negative_00855():
    with pytest.raises(ValueError):
        price_with_tax_00855(1000, -1)


def test_is_valid_sku_00855():
    assert is_valid_sku_00855("abc123")
    assert not is_valid_sku_00855("")


def test_bucket_by_tag_00855():
    p = Product_00855("s1", 100, ["a"])
    assert bucket_by_tag_00855([p]) == {"a": ["s1"]}
