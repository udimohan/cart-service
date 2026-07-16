"""Tests for catalog_00573."""

import pytest

from cartservice.generated.catalog_00573 import (
    Product_00573,
    bucket_by_tag_00573,
    is_valid_sku_00573,
    price_with_tax_00573,
)


def test_price_with_tax_00573():
    assert price_with_tax_00573(1000, 500) == 1050


def test_price_with_tax_negative_00573():
    with pytest.raises(ValueError):
        price_with_tax_00573(1000, -1)


def test_is_valid_sku_00573():
    assert is_valid_sku_00573("abc123")
    assert not is_valid_sku_00573("")


def test_bucket_by_tag_00573():
    p = Product_00573("s1", 100, ["a"])
    assert bucket_by_tag_00573([p]) == {"a": ["s1"]}
