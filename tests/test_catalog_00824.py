"""Tests for catalog_00824."""

import pytest

from cartservice.generated.catalog_00824 import (
    Product_00824,
    bucket_by_tag_00824,
    is_valid_sku_00824,
    price_with_tax_00824,
)


def test_price_with_tax_00824():
    assert price_with_tax_00824(1000, 500) == 1050


def test_price_with_tax_negative_00824():
    with pytest.raises(ValueError):
        price_with_tax_00824(1000, -1)


def test_is_valid_sku_00824():
    assert is_valid_sku_00824("abc123")
    assert not is_valid_sku_00824("")


def test_bucket_by_tag_00824():
    p = Product_00824("s1", 100, ["a"])
    assert bucket_by_tag_00824([p]) == {"a": ["s1"]}
