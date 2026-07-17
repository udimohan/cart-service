"""Tests for catalog_00199."""

import pytest

from cartservice.generated.catalog_00199 import (
    Product_00199,
    bucket_by_tag_00199,
    is_valid_sku_00199,
    price_with_tax_00199,
)


def test_price_with_tax_00199():
    assert price_with_tax_00199(1000, 500) == 1050


def test_price_with_tax_negative_00199():
    with pytest.raises(ValueError):
        price_with_tax_00199(1000, -1)


def test_is_valid_sku_00199():
    assert is_valid_sku_00199("abc123")
    assert not is_valid_sku_00199("")


def test_bucket_by_tag_00199():
    p = Product_00199("s1", 100, ["a"])
    assert bucket_by_tag_00199([p]) == {"a": ["s1"]}
