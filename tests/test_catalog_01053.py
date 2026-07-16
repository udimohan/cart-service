"""Tests for catalog_01053."""

import pytest

from cartservice.generated.catalog_01053 import (
    Product_01053,
    bucket_by_tag_01053,
    is_valid_sku_01053,
    price_with_tax_01053,
)


def test_price_with_tax_01053():
    assert price_with_tax_01053(1000, 500) == 1050


def test_price_with_tax_negative_01053():
    with pytest.raises(ValueError):
        price_with_tax_01053(1000, -1)


def test_is_valid_sku_01053():
    assert is_valid_sku_01053("abc123")
    assert not is_valid_sku_01053("")


def test_bucket_by_tag_01053():
    p = Product_01053("s1", 100, ["a"])
    assert bucket_by_tag_01053([p]) == {"a": ["s1"]}
