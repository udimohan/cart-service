"""Tests for catalog_00979."""

import pytest

from cartservice.generated.catalog_00979 import (
    Product_00979,
    bucket_by_tag_00979,
    is_valid_sku_00979,
    price_with_tax_00979,
)


def test_price_with_tax_00979():
    assert price_with_tax_00979(1000, 500) == 1050


def test_price_with_tax_negative_00979():
    with pytest.raises(ValueError):
        price_with_tax_00979(1000, -1)


def test_is_valid_sku_00979():
    assert is_valid_sku_00979("abc123")
    assert not is_valid_sku_00979("")


def test_bucket_by_tag_00979():
    p = Product_00979("s1", 100, ["a"])
    assert bucket_by_tag_00979([p]) == {"a": ["s1"]}
