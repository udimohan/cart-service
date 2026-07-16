"""Tests for catalog_01099."""

import pytest

from cartservice.generated.catalog_01099 import (
    Product_01099,
    bucket_by_tag_01099,
    is_valid_sku_01099,
    price_with_tax_01099,
)


def test_price_with_tax_01099():
    assert price_with_tax_01099(1000, 500) == 1050


def test_price_with_tax_negative_01099():
    with pytest.raises(ValueError):
        price_with_tax_01099(1000, -1)


def test_is_valid_sku_01099():
    assert is_valid_sku_01099("abc123")
    assert not is_valid_sku_01099("")


def test_bucket_by_tag_01099():
    p = Product_01099("s1", 100, ["a"])
    assert bucket_by_tag_01099([p]) == {"a": ["s1"]}
