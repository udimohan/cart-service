"""Tests for catalog_00763."""

import pytest

from cartservice.generated.catalog_00763 import (
    Product_00763,
    bucket_by_tag_00763,
    is_valid_sku_00763,
    price_with_tax_00763,
)


def test_price_with_tax_00763():
    assert price_with_tax_00763(1000, 500) == 1050


def test_price_with_tax_negative_00763():
    with pytest.raises(ValueError):
        price_with_tax_00763(1000, -1)


def test_is_valid_sku_00763():
    assert is_valid_sku_00763("abc123")
    assert not is_valid_sku_00763("")


def test_bucket_by_tag_00763():
    p = Product_00763("s1", 100, ["a"])
    assert bucket_by_tag_00763([p]) == {"a": ["s1"]}
