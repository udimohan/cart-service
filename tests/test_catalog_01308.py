"""Tests for catalog_01308."""

import pytest

from cartservice.generated.catalog_01308 import (
    Product_01308,
    bucket_by_tag_01308,
    is_valid_sku_01308,
    price_with_tax_01308,
)


def test_price_with_tax_01308():
    assert price_with_tax_01308(1000, 500) == 1050


def test_price_with_tax_negative_01308():
    with pytest.raises(ValueError):
        price_with_tax_01308(1000, -1)


def test_is_valid_sku_01308():
    assert is_valid_sku_01308("abc123")
    assert not is_valid_sku_01308("")


def test_bucket_by_tag_01308():
    p = Product_01308("s1", 100, ["a"])
    assert bucket_by_tag_01308([p]) == {"a": ["s1"]}
