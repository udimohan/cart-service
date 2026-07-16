"""Tests for catalog_01553."""

import pytest

from cartservice.generated.catalog_01553 import (
    Product_01553,
    bucket_by_tag_01553,
    is_valid_sku_01553,
    price_with_tax_01553,
)


def test_price_with_tax_01553():
    assert price_with_tax_01553(1000, 500) == 1050


def test_price_with_tax_negative_01553():
    with pytest.raises(ValueError):
        price_with_tax_01553(1000, -1)


def test_is_valid_sku_01553():
    assert is_valid_sku_01553("abc123")
    assert not is_valid_sku_01553("")


def test_bucket_by_tag_01553():
    p = Product_01553("s1", 100, ["a"])
    assert bucket_by_tag_01553([p]) == {"a": ["s1"]}
