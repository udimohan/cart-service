"""Tests for catalog_01209."""

import pytest

from cartservice.generated.catalog_01209 import (
    Product_01209,
    bucket_by_tag_01209,
    is_valid_sku_01209,
    price_with_tax_01209,
)


def test_price_with_tax_01209():
    assert price_with_tax_01209(1000, 500) == 1050


def test_price_with_tax_negative_01209():
    with pytest.raises(ValueError):
        price_with_tax_01209(1000, -1)


def test_is_valid_sku_01209():
    assert is_valid_sku_01209("abc123")
    assert not is_valid_sku_01209("")


def test_bucket_by_tag_01209():
    p = Product_01209("s1", 100, ["a"])
    assert bucket_by_tag_01209([p]) == {"a": ["s1"]}
