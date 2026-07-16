"""Tests for catalog_01244."""

import pytest

from cartservice.generated.catalog_01244 import (
    Product_01244,
    bucket_by_tag_01244,
    is_valid_sku_01244,
    price_with_tax_01244,
)


def test_price_with_tax_01244():
    assert price_with_tax_01244(1000, 500) == 1050


def test_price_with_tax_negative_01244():
    with pytest.raises(ValueError):
        price_with_tax_01244(1000, -1)


def test_is_valid_sku_01244():
    assert is_valid_sku_01244("abc123")
    assert not is_valid_sku_01244("")


def test_bucket_by_tag_01244():
    p = Product_01244("s1", 100, ["a"])
    assert bucket_by_tag_01244([p]) == {"a": ["s1"]}
