"""Tests for catalog_01144."""

import pytest

from cartservice.generated.catalog_01144 import (
    Product_01144,
    bucket_by_tag_01144,
    is_valid_sku_01144,
    price_with_tax_01144,
)


def test_price_with_tax_01144():
    assert price_with_tax_01144(1000, 500) == 1050


def test_price_with_tax_negative_01144():
    with pytest.raises(ValueError):
        price_with_tax_01144(1000, -1)


def test_is_valid_sku_01144():
    assert is_valid_sku_01144("abc123")
    assert not is_valid_sku_01144("")


def test_bucket_by_tag_01144():
    p = Product_01144("s1", 100, ["a"])
    assert bucket_by_tag_01144([p]) == {"a": ["s1"]}
