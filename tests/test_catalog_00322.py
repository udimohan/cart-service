"""Tests for catalog_00322."""

import pytest

from cartservice.generated.catalog_00322 import (
    Product_00322,
    bucket_by_tag_00322,
    is_valid_sku_00322,
    price_with_tax_00322,
)


def test_price_with_tax_00322():
    assert price_with_tax_00322(1000, 500) == 1050


def test_price_with_tax_negative_00322():
    with pytest.raises(ValueError):
        price_with_tax_00322(1000, -1)


def test_is_valid_sku_00322():
    assert is_valid_sku_00322("abc123")
    assert not is_valid_sku_00322("")


def test_bucket_by_tag_00322():
    p = Product_00322("s1", 100, ["a"])
    assert bucket_by_tag_00322([p]) == {"a": ["s1"]}
