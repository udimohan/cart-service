"""Tests for catalog_01678."""

import pytest

from cartservice.generated.catalog_01678 import (
    Product_01678,
    bucket_by_tag_01678,
    is_valid_sku_01678,
    price_with_tax_01678,
)


def test_price_with_tax_01678():
    assert price_with_tax_01678(1000, 500) == 1050


def test_price_with_tax_negative_01678():
    with pytest.raises(ValueError):
        price_with_tax_01678(1000, -1)


def test_is_valid_sku_01678():
    assert is_valid_sku_01678("abc123")
    assert not is_valid_sku_01678("")


def test_bucket_by_tag_01678():
    p = Product_01678("s1", 100, ["a"])
    assert bucket_by_tag_01678([p]) == {"a": ["s1"]}
