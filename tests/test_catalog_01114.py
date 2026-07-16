"""Tests for catalog_01114."""

import pytest

from cartservice.generated.catalog_01114 import (
    Product_01114,
    bucket_by_tag_01114,
    is_valid_sku_01114,
    price_with_tax_01114,
)


def test_price_with_tax_01114():
    assert price_with_tax_01114(1000, 500) == 1050


def test_price_with_tax_negative_01114():
    with pytest.raises(ValueError):
        price_with_tax_01114(1000, -1)


def test_is_valid_sku_01114():
    assert is_valid_sku_01114("abc123")
    assert not is_valid_sku_01114("")


def test_bucket_by_tag_01114():
    p = Product_01114("s1", 100, ["a"])
    assert bucket_by_tag_01114([p]) == {"a": ["s1"]}
