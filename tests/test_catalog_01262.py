"""Tests for catalog_01262."""

import pytest

from cartservice.generated.catalog_01262 import (
    Product_01262,
    bucket_by_tag_01262,
    is_valid_sku_01262,
    price_with_tax_01262,
)


def test_price_with_tax_01262():
    assert price_with_tax_01262(1000, 500) == 1050


def test_price_with_tax_negative_01262():
    with pytest.raises(ValueError):
        price_with_tax_01262(1000, -1)


def test_is_valid_sku_01262():
    assert is_valid_sku_01262("abc123")
    assert not is_valid_sku_01262("")


def test_bucket_by_tag_01262():
    p = Product_01262("s1", 100, ["a"])
    assert bucket_by_tag_01262([p]) == {"a": ["s1"]}
