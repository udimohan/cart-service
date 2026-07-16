"""Tests for catalog_01539."""

import pytest

from cartservice.generated.catalog_01539 import (
    Product_01539,
    bucket_by_tag_01539,
    is_valid_sku_01539,
    price_with_tax_01539,
)


def test_price_with_tax_01539():
    assert price_with_tax_01539(1000, 500) == 1050


def test_price_with_tax_negative_01539():
    with pytest.raises(ValueError):
        price_with_tax_01539(1000, -1)


def test_is_valid_sku_01539():
    assert is_valid_sku_01539("abc123")
    assert not is_valid_sku_01539("")


def test_bucket_by_tag_01539():
    p = Product_01539("s1", 100, ["a"])
    assert bucket_by_tag_01539([p]) == {"a": ["s1"]}
