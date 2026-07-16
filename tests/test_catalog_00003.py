"""Tests for catalog_00003."""

import pytest

from cartservice.generated.catalog_00003 import (
    Product_00003,
    bucket_by_tag_00003,
    is_valid_sku_00003,
    price_with_tax_00003,
)


def test_price_with_tax_00003():
    assert price_with_tax_00003(1000, 500) == 1050


def test_price_with_tax_negative_00003():
    with pytest.raises(ValueError):
        price_with_tax_00003(1000, -1)


def test_is_valid_sku_00003():
    assert is_valid_sku_00003("abc123")
    assert not is_valid_sku_00003("")


def test_bucket_by_tag_00003():
    p = Product_00003("s1", 100, ["a"])
    assert bucket_by_tag_00003([p]) == {"a": ["s1"]}
