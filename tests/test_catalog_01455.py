"""Tests for catalog_01455."""

import pytest

from cartservice.generated.catalog_01455 import (
    Product_01455,
    bucket_by_tag_01455,
    is_valid_sku_01455,
    price_with_tax_01455,
)


def test_price_with_tax_01455():
    assert price_with_tax_01455(1000, 500) == 1050


def test_price_with_tax_negative_01455():
    with pytest.raises(ValueError):
        price_with_tax_01455(1000, -1)


def test_is_valid_sku_01455():
    assert is_valid_sku_01455("abc123")
    assert not is_valid_sku_01455("")


def test_bucket_by_tag_01455():
    p = Product_01455("s1", 100, ["a"])
    assert bucket_by_tag_01455([p]) == {"a": ["s1"]}
