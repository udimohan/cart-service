"""Tests for catalog_01380."""

import pytest

from cartservice.generated.catalog_01380 import (
    Product_01380,
    bucket_by_tag_01380,
    is_valid_sku_01380,
    price_with_tax_01380,
)


def test_price_with_tax_01380():
    assert price_with_tax_01380(1000, 500) == 1050


def test_price_with_tax_negative_01380():
    with pytest.raises(ValueError):
        price_with_tax_01380(1000, -1)


def test_is_valid_sku_01380():
    assert is_valid_sku_01380("abc123")
    assert not is_valid_sku_01380("")


def test_bucket_by_tag_01380():
    p = Product_01380("s1", 100, ["a"])
    assert bucket_by_tag_01380([p]) == {"a": ["s1"]}
