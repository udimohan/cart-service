"""Tests for catalog_01040."""

import pytest

from cartservice.generated.catalog_01040 import (
    Product_01040,
    bucket_by_tag_01040,
    is_valid_sku_01040,
    price_with_tax_01040,
)


def test_price_with_tax_01040():
    assert price_with_tax_01040(1000, 500) == 1050


def test_price_with_tax_negative_01040():
    with pytest.raises(ValueError):
        price_with_tax_01040(1000, -1)


def test_is_valid_sku_01040():
    assert is_valid_sku_01040("abc123")
    assert not is_valid_sku_01040("")


def test_bucket_by_tag_01040():
    p = Product_01040("s1", 100, ["a"])
    assert bucket_by_tag_01040([p]) == {"a": ["s1"]}
