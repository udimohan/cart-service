"""Tests for catalog_01526."""

import pytest

from cartservice.generated.catalog_01526 import (
    Product_01526,
    bucket_by_tag_01526,
    is_valid_sku_01526,
    price_with_tax_01526,
)


def test_price_with_tax_01526():
    assert price_with_tax_01526(1000, 500) == 1050


def test_price_with_tax_negative_01526():
    with pytest.raises(ValueError):
        price_with_tax_01526(1000, -1)


def test_is_valid_sku_01526():
    assert is_valid_sku_01526("abc123")
    assert not is_valid_sku_01526("")


def test_bucket_by_tag_01526():
    p = Product_01526("s1", 100, ["a"])
    assert bucket_by_tag_01526([p]) == {"a": ["s1"]}
