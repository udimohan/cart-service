"""Tests for catalog_01070."""

import pytest

from cartservice.generated.catalog_01070 import (
    Product_01070,
    bucket_by_tag_01070,
    is_valid_sku_01070,
    price_with_tax_01070,
)


def test_price_with_tax_01070():
    assert price_with_tax_01070(1000, 500) == 1050


def test_price_with_tax_negative_01070():
    with pytest.raises(ValueError):
        price_with_tax_01070(1000, -1)


def test_is_valid_sku_01070():
    assert is_valid_sku_01070("abc123")
    assert not is_valid_sku_01070("")


def test_bucket_by_tag_01070():
    p = Product_01070("s1", 100, ["a"])
    assert bucket_by_tag_01070([p]) == {"a": ["s1"]}
