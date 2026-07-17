"""Tests for catalog_00069."""

import pytest

from cartservice.generated.catalog_00069 import (
    Product_00069,
    bucket_by_tag_00069,
    is_valid_sku_00069,
    price_with_tax_00069,
)


def test_price_with_tax_00069():
    assert price_with_tax_00069(1000, 500) == 1050


def test_price_with_tax_negative_00069():
    with pytest.raises(ValueError):
        price_with_tax_00069(1000, -1)


def test_is_valid_sku_00069():
    assert is_valid_sku_00069("abc123")
    assert not is_valid_sku_00069("")


def test_bucket_by_tag_00069():
    p = Product_00069("s1", 100, ["a"])
    assert bucket_by_tag_00069([p]) == {"a": ["s1"]}
