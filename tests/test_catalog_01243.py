"""Tests for catalog_01243."""

import pytest

from cartservice.generated.catalog_01243 import (
    Product_01243,
    bucket_by_tag_01243,
    is_valid_sku_01243,
    price_with_tax_01243,
)


def test_price_with_tax_01243():
    assert price_with_tax_01243(1000, 500) == 1050


def test_price_with_tax_negative_01243():
    with pytest.raises(ValueError):
        price_with_tax_01243(1000, -1)


def test_is_valid_sku_01243():
    assert is_valid_sku_01243("abc123")
    assert not is_valid_sku_01243("")


def test_bucket_by_tag_01243():
    p = Product_01243("s1", 100, ["a"])
    assert bucket_by_tag_01243([p]) == {"a": ["s1"]}
