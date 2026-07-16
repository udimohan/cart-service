"""Tests for catalog_01499."""

import pytest

from cartservice.generated.catalog_01499 import (
    Product_01499,
    bucket_by_tag_01499,
    is_valid_sku_01499,
    price_with_tax_01499,
)


def test_price_with_tax_01499():
    assert price_with_tax_01499(1000, 500) == 1050


def test_price_with_tax_negative_01499():
    with pytest.raises(ValueError):
        price_with_tax_01499(1000, -1)


def test_is_valid_sku_01499():
    assert is_valid_sku_01499("abc123")
    assert not is_valid_sku_01499("")


def test_bucket_by_tag_01499():
    p = Product_01499("s1", 100, ["a"])
    assert bucket_by_tag_01499([p]) == {"a": ["s1"]}
