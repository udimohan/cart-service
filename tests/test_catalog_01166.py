"""Tests for catalog_01166."""

import pytest

from cartservice.generated.catalog_01166 import (
    Product_01166,
    bucket_by_tag_01166,
    is_valid_sku_01166,
    price_with_tax_01166,
)


def test_price_with_tax_01166():
    assert price_with_tax_01166(1000, 500) == 1050


def test_price_with_tax_negative_01166():
    with pytest.raises(ValueError):
        price_with_tax_01166(1000, -1)


def test_is_valid_sku_01166():
    assert is_valid_sku_01166("abc123")
    assert not is_valid_sku_01166("")


def test_bucket_by_tag_01166():
    p = Product_01166("s1", 100, ["a"])
    assert bucket_by_tag_01166([p]) == {"a": ["s1"]}
