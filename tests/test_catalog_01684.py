"""Tests for catalog_01684."""

import pytest

from cartservice.generated.catalog_01684 import (
    Product_01684,
    bucket_by_tag_01684,
    is_valid_sku_01684,
    price_with_tax_01684,
)


def test_price_with_tax_01684():
    assert price_with_tax_01684(1000, 500) == 1050


def test_price_with_tax_negative_01684():
    with pytest.raises(ValueError):
        price_with_tax_01684(1000, -1)


def test_is_valid_sku_01684():
    assert is_valid_sku_01684("abc123")
    assert not is_valid_sku_01684("")


def test_bucket_by_tag_01684():
    p = Product_01684("s1", 100, ["a"])
    assert bucket_by_tag_01684([p]) == {"a": ["s1"]}
