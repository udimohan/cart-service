"""Tests for catalog_01064."""

import pytest

from cartservice.generated.catalog_01064 import (
    Product_01064,
    bucket_by_tag_01064,
    is_valid_sku_01064,
    price_with_tax_01064,
)


def test_price_with_tax_01064():
    assert price_with_tax_01064(1000, 500) == 1050


def test_price_with_tax_negative_01064():
    with pytest.raises(ValueError):
        price_with_tax_01064(1000, -1)


def test_is_valid_sku_01064():
    assert is_valid_sku_01064("abc123")
    assert not is_valid_sku_01064("")


def test_bucket_by_tag_01064():
    p = Product_01064("s1", 100, ["a"])
    assert bucket_by_tag_01064([p]) == {"a": ["s1"]}
