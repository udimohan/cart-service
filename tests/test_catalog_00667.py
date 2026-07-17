"""Tests for catalog_00667."""

import pytest

from cartservice.generated.catalog_00667 import (
    Product_00667,
    bucket_by_tag_00667,
    is_valid_sku_00667,
    price_with_tax_00667,
)


def test_price_with_tax_00667():
    assert price_with_tax_00667(1000, 500) == 1050


def test_price_with_tax_negative_00667():
    with pytest.raises(ValueError):
        price_with_tax_00667(1000, -1)


def test_is_valid_sku_00667():
    assert is_valid_sku_00667("abc123")
    assert not is_valid_sku_00667("")


def test_bucket_by_tag_00667():
    p = Product_00667("s1", 100, ["a"])
    assert bucket_by_tag_00667([p]) == {"a": ["s1"]}
