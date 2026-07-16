"""Tests for catalog_01176."""

import pytest

from cartservice.generated.catalog_01176 import (
    Product_01176,
    bucket_by_tag_01176,
    is_valid_sku_01176,
    price_with_tax_01176,
)


def test_price_with_tax_01176():
    assert price_with_tax_01176(1000, 500) == 1050


def test_price_with_tax_negative_01176():
    with pytest.raises(ValueError):
        price_with_tax_01176(1000, -1)


def test_is_valid_sku_01176():
    assert is_valid_sku_01176("abc123")
    assert not is_valid_sku_01176("")


def test_bucket_by_tag_01176():
    p = Product_01176("s1", 100, ["a"])
    assert bucket_by_tag_01176([p]) == {"a": ["s1"]}
