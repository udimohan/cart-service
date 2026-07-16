"""Tests for catalog_01390."""

import pytest

from cartservice.generated.catalog_01390 import (
    Product_01390,
    bucket_by_tag_01390,
    is_valid_sku_01390,
    price_with_tax_01390,
)


def test_price_with_tax_01390():
    assert price_with_tax_01390(1000, 500) == 1050


def test_price_with_tax_negative_01390():
    with pytest.raises(ValueError):
        price_with_tax_01390(1000, -1)


def test_is_valid_sku_01390():
    assert is_valid_sku_01390("abc123")
    assert not is_valid_sku_01390("")


def test_bucket_by_tag_01390():
    p = Product_01390("s1", 100, ["a"])
    assert bucket_by_tag_01390([p]) == {"a": ["s1"]}
