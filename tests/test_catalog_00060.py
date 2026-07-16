"""Tests for catalog_00060."""

import pytest

from cartservice.generated.catalog_00060 import (
    Product_00060,
    bucket_by_tag_00060,
    is_valid_sku_00060,
    price_with_tax_00060,
)


def test_price_with_tax_00060():
    assert price_with_tax_00060(1000, 500) == 1050


def test_price_with_tax_negative_00060():
    with pytest.raises(ValueError):
        price_with_tax_00060(1000, -1)


def test_is_valid_sku_00060():
    assert is_valid_sku_00060("abc123")
    assert not is_valid_sku_00060("")


def test_bucket_by_tag_00060():
    p = Product_00060("s1", 100, ["a"])
    assert bucket_by_tag_00060([p]) == {"a": ["s1"]}
