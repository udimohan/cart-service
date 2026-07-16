"""Tests for catalog_00865."""

import pytest

from cartservice.generated.catalog_00865 import (
    Product_00865,
    bucket_by_tag_00865,
    is_valid_sku_00865,
    price_with_tax_00865,
)


def test_price_with_tax_00865():
    assert price_with_tax_00865(1000, 500) == 1050


def test_price_with_tax_negative_00865():
    with pytest.raises(ValueError):
        price_with_tax_00865(1000, -1)


def test_is_valid_sku_00865():
    assert is_valid_sku_00865("abc123")
    assert not is_valid_sku_00865("")


def test_bucket_by_tag_00865():
    p = Product_00865("s1", 100, ["a"])
    assert bucket_by_tag_00865([p]) == {"a": ["s1"]}
