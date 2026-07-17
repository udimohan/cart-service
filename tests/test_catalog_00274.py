"""Tests for catalog_00274."""

import pytest

from cartservice.generated.catalog_00274 import (
    Product_00274,
    bucket_by_tag_00274,
    is_valid_sku_00274,
    price_with_tax_00274,
)


def test_price_with_tax_00274():
    assert price_with_tax_00274(1000, 500) == 1050


def test_price_with_tax_negative_00274():
    with pytest.raises(ValueError):
        price_with_tax_00274(1000, -1)


def test_is_valid_sku_00274():
    assert is_valid_sku_00274("abc123")
    assert not is_valid_sku_00274("")


def test_bucket_by_tag_00274():
    p = Product_00274("s1", 100, ["a"])
    assert bucket_by_tag_00274([p]) == {"a": ["s1"]}
