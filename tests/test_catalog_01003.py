"""Tests for catalog_01003."""

import pytest

from cartservice.generated.catalog_01003 import (
    Product_01003,
    bucket_by_tag_01003,
    is_valid_sku_01003,
    price_with_tax_01003,
)


def test_price_with_tax_01003():
    assert price_with_tax_01003(1000, 500) == 1050


def test_price_with_tax_negative_01003():
    with pytest.raises(ValueError):
        price_with_tax_01003(1000, -1)


def test_is_valid_sku_01003():
    assert is_valid_sku_01003("abc123")
    assert not is_valid_sku_01003("")


def test_bucket_by_tag_01003():
    p = Product_01003("s1", 100, ["a"])
    assert bucket_by_tag_01003([p]) == {"a": ["s1"]}
