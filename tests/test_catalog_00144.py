"""Tests for catalog_00144."""

import pytest

from cartservice.generated.catalog_00144 import (
    Product_00144,
    bucket_by_tag_00144,
    is_valid_sku_00144,
    price_with_tax_00144,
)


def test_price_with_tax_00144():
    assert price_with_tax_00144(1000, 500) == 1050


def test_price_with_tax_negative_00144():
    with pytest.raises(ValueError):
        price_with_tax_00144(1000, -1)


def test_is_valid_sku_00144():
    assert is_valid_sku_00144("abc123")
    assert not is_valid_sku_00144("")


def test_bucket_by_tag_00144():
    p = Product_00144("s1", 100, ["a"])
    assert bucket_by_tag_00144([p]) == {"a": ["s1"]}
