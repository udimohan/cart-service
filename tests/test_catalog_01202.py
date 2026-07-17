"""Tests for catalog_01202."""

import pytest

from cartservice.generated.catalog_01202 import (
    Product_01202,
    bucket_by_tag_01202,
    is_valid_sku_01202,
    price_with_tax_01202,
)


def test_price_with_tax_01202():
    assert price_with_tax_01202(1000, 500) == 1050


def test_price_with_tax_negative_01202():
    with pytest.raises(ValueError):
        price_with_tax_01202(1000, -1)


def test_is_valid_sku_01202():
    assert is_valid_sku_01202("abc123")
    assert not is_valid_sku_01202("")


def test_bucket_by_tag_01202():
    p = Product_01202("s1", 100, ["a"])
    assert bucket_by_tag_01202([p]) == {"a": ["s1"]}
