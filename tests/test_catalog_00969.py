"""Tests for catalog_00969."""

import pytest

from cartservice.generated.catalog_00969 import (
    Product_00969,
    bucket_by_tag_00969,
    is_valid_sku_00969,
    price_with_tax_00969,
)


def test_price_with_tax_00969():
    assert price_with_tax_00969(1000, 500) == 1050


def test_price_with_tax_negative_00969():
    with pytest.raises(ValueError):
        price_with_tax_00969(1000, -1)


def test_is_valid_sku_00969():
    assert is_valid_sku_00969("abc123")
    assert not is_valid_sku_00969("")


def test_bucket_by_tag_00969():
    p = Product_00969("s1", 100, ["a"])
    assert bucket_by_tag_00969([p]) == {"a": ["s1"]}
