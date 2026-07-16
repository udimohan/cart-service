"""Tests for catalog_01694."""

import pytest

from cartservice.generated.catalog_01694 import (
    Product_01694,
    bucket_by_tag_01694,
    is_valid_sku_01694,
    price_with_tax_01694,
)


def test_price_with_tax_01694():
    assert price_with_tax_01694(1000, 500) == 1050


def test_price_with_tax_negative_01694():
    with pytest.raises(ValueError):
        price_with_tax_01694(1000, -1)


def test_is_valid_sku_01694():
    assert is_valid_sku_01694("abc123")
    assert not is_valid_sku_01694("")


def test_bucket_by_tag_01694():
    p = Product_01694("s1", 100, ["a"])
    assert bucket_by_tag_01694([p]) == {"a": ["s1"]}
