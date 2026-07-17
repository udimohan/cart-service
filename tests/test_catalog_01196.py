"""Tests for catalog_01196."""

import pytest

from cartservice.generated.catalog_01196 import (
    Product_01196,
    bucket_by_tag_01196,
    is_valid_sku_01196,
    price_with_tax_01196,
)


def test_price_with_tax_01196():
    assert price_with_tax_01196(1000, 500) == 1050


def test_price_with_tax_negative_01196():
    with pytest.raises(ValueError):
        price_with_tax_01196(1000, -1)


def test_is_valid_sku_01196():
    assert is_valid_sku_01196("abc123")
    assert not is_valid_sku_01196("")


def test_bucket_by_tag_01196():
    p = Product_01196("s1", 100, ["a"])
    assert bucket_by_tag_01196([p]) == {"a": ["s1"]}
