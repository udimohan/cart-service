"""Tests for catalog_01015."""

import pytest

from cartservice.generated.catalog_01015 import (
    Product_01015,
    bucket_by_tag_01015,
    is_valid_sku_01015,
    price_with_tax_01015,
)


def test_price_with_tax_01015():
    assert price_with_tax_01015(1000, 500) == 1050


def test_price_with_tax_negative_01015():
    with pytest.raises(ValueError):
        price_with_tax_01015(1000, -1)


def test_is_valid_sku_01015():
    assert is_valid_sku_01015("abc123")
    assert not is_valid_sku_01015("")


def test_bucket_by_tag_01015():
    p = Product_01015("s1", 100, ["a"])
    assert bucket_by_tag_01015([p]) == {"a": ["s1"]}
