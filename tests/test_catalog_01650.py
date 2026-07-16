"""Tests for catalog_01650."""

import pytest

from cartservice.generated.catalog_01650 import (
    Product_01650,
    bucket_by_tag_01650,
    is_valid_sku_01650,
    price_with_tax_01650,
)


def test_price_with_tax_01650():
    assert price_with_tax_01650(1000, 500) == 1050


def test_price_with_tax_negative_01650():
    with pytest.raises(ValueError):
        price_with_tax_01650(1000, -1)


def test_is_valid_sku_01650():
    assert is_valid_sku_01650("abc123")
    assert not is_valid_sku_01650("")


def test_bucket_by_tag_01650():
    p = Product_01650("s1", 100, ["a"])
    assert bucket_by_tag_01650([p]) == {"a": ["s1"]}
