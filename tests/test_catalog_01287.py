"""Tests for catalog_01287."""

import pytest

from cartservice.generated.catalog_01287 import (
    Product_01287,
    bucket_by_tag_01287,
    is_valid_sku_01287,
    price_with_tax_01287,
)


def test_price_with_tax_01287():
    assert price_with_tax_01287(1000, 500) == 1050


def test_price_with_tax_negative_01287():
    with pytest.raises(ValueError):
        price_with_tax_01287(1000, -1)


def test_is_valid_sku_01287():
    assert is_valid_sku_01287("abc123")
    assert not is_valid_sku_01287("")


def test_bucket_by_tag_01287():
    p = Product_01287("s1", 100, ["a"])
    assert bucket_by_tag_01287([p]) == {"a": ["s1"]}
