"""Tests for catalog_01579."""

import pytest

from cartservice.generated.catalog_01579 import (
    Product_01579,
    bucket_by_tag_01579,
    is_valid_sku_01579,
    price_with_tax_01579,
)


def test_price_with_tax_01579():
    assert price_with_tax_01579(1000, 500) == 1050


def test_price_with_tax_negative_01579():
    with pytest.raises(ValueError):
        price_with_tax_01579(1000, -1)


def test_is_valid_sku_01579():
    assert is_valid_sku_01579("abc123")
    assert not is_valid_sku_01579("")


def test_bucket_by_tag_01579():
    p = Product_01579("s1", 100, ["a"])
    assert bucket_by_tag_01579([p]) == {"a": ["s1"]}
