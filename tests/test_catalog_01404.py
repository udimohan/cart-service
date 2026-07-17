"""Tests for catalog_01404."""

import pytest

from cartservice.generated.catalog_01404 import (
    Product_01404,
    bucket_by_tag_01404,
    is_valid_sku_01404,
    price_with_tax_01404,
)


def test_price_with_tax_01404():
    assert price_with_tax_01404(1000, 500) == 1050


def test_price_with_tax_negative_01404():
    with pytest.raises(ValueError):
        price_with_tax_01404(1000, -1)


def test_is_valid_sku_01404():
    assert is_valid_sku_01404("abc123")
    assert not is_valid_sku_01404("")


def test_bucket_by_tag_01404():
    p = Product_01404("s1", 100, ["a"])
    assert bucket_by_tag_01404([p]) == {"a": ["s1"]}
