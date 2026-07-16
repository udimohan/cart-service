"""Tests for catalog_01265."""

import pytest

from cartservice.generated.catalog_01265 import (
    Product_01265,
    bucket_by_tag_01265,
    is_valid_sku_01265,
    price_with_tax_01265,
)


def test_price_with_tax_01265():
    assert price_with_tax_01265(1000, 500) == 1050


def test_price_with_tax_negative_01265():
    with pytest.raises(ValueError):
        price_with_tax_01265(1000, -1)


def test_is_valid_sku_01265():
    assert is_valid_sku_01265("abc123")
    assert not is_valid_sku_01265("")


def test_bucket_by_tag_01265():
    p = Product_01265("s1", 100, ["a"])
    assert bucket_by_tag_01265([p]) == {"a": ["s1"]}
