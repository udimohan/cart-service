"""Tests for catalog_01696."""

import pytest

from cartservice.generated.catalog_01696 import (
    Product_01696,
    bucket_by_tag_01696,
    is_valid_sku_01696,
    price_with_tax_01696,
)


def test_price_with_tax_01696():
    assert price_with_tax_01696(1000, 500) == 1050


def test_price_with_tax_negative_01696():
    with pytest.raises(ValueError):
        price_with_tax_01696(1000, -1)


def test_is_valid_sku_01696():
    assert is_valid_sku_01696("abc123")
    assert not is_valid_sku_01696("")


def test_bucket_by_tag_01696():
    p = Product_01696("s1", 100, ["a"])
    assert bucket_by_tag_01696([p]) == {"a": ["s1"]}
