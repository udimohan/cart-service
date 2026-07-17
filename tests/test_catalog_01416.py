"""Tests for catalog_01416."""

import pytest

from cartservice.generated.catalog_01416 import (
    Product_01416,
    bucket_by_tag_01416,
    is_valid_sku_01416,
    price_with_tax_01416,
)


def test_price_with_tax_01416():
    assert price_with_tax_01416(1000, 500) == 1050


def test_price_with_tax_negative_01416():
    with pytest.raises(ValueError):
        price_with_tax_01416(1000, -1)


def test_is_valid_sku_01416():
    assert is_valid_sku_01416("abc123")
    assert not is_valid_sku_01416("")


def test_bucket_by_tag_01416():
    p = Product_01416("s1", 100, ["a"])
    assert bucket_by_tag_01416([p]) == {"a": ["s1"]}
