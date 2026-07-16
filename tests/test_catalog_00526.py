"""Tests for catalog_00526."""

import pytest

from cartservice.generated.catalog_00526 import (
    Product_00526,
    bucket_by_tag_00526,
    is_valid_sku_00526,
    price_with_tax_00526,
)


def test_price_with_tax_00526():
    assert price_with_tax_00526(1000, 500) == 1050


def test_price_with_tax_negative_00526():
    with pytest.raises(ValueError):
        price_with_tax_00526(1000, -1)


def test_is_valid_sku_00526():
    assert is_valid_sku_00526("abc123")
    assert not is_valid_sku_00526("")


def test_bucket_by_tag_00526():
    p = Product_00526("s1", 100, ["a"])
    assert bucket_by_tag_00526([p]) == {"a": ["s1"]}
