"""Tests for catalog_00656."""

import pytest

from cartservice.generated.catalog_00656 import (
    Product_00656,
    bucket_by_tag_00656,
    is_valid_sku_00656,
    price_with_tax_00656,
)


def test_price_with_tax_00656():
    assert price_with_tax_00656(1000, 500) == 1050


def test_price_with_tax_negative_00656():
    with pytest.raises(ValueError):
        price_with_tax_00656(1000, -1)


def test_is_valid_sku_00656():
    assert is_valid_sku_00656("abc123")
    assert not is_valid_sku_00656("")


def test_bucket_by_tag_00656():
    p = Product_00656("s1", 100, ["a"])
    assert bucket_by_tag_00656([p]) == {"a": ["s1"]}
