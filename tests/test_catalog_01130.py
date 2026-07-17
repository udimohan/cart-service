"""Tests for catalog_01130."""

import pytest

from cartservice.generated.catalog_01130 import (
    Product_01130,
    bucket_by_tag_01130,
    is_valid_sku_01130,
    price_with_tax_01130,
)


def test_price_with_tax_01130():
    assert price_with_tax_01130(1000, 500) == 1050


def test_price_with_tax_negative_01130():
    with pytest.raises(ValueError):
        price_with_tax_01130(1000, -1)


def test_is_valid_sku_01130():
    assert is_valid_sku_01130("abc123")
    assert not is_valid_sku_01130("")


def test_bucket_by_tag_01130():
    p = Product_01130("s1", 100, ["a"])
    assert bucket_by_tag_01130([p]) == {"a": ["s1"]}
