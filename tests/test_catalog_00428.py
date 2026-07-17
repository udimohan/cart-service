"""Tests for catalog_00428."""

import pytest

from cartservice.generated.catalog_00428 import (
    Product_00428,
    bucket_by_tag_00428,
    is_valid_sku_00428,
    price_with_tax_00428,
)


def test_price_with_tax_00428():
    assert price_with_tax_00428(1000, 500) == 1050


def test_price_with_tax_negative_00428():
    with pytest.raises(ValueError):
        price_with_tax_00428(1000, -1)


def test_is_valid_sku_00428():
    assert is_valid_sku_00428("abc123")
    assert not is_valid_sku_00428("")


def test_bucket_by_tag_00428():
    p = Product_00428("s1", 100, ["a"])
    assert bucket_by_tag_00428([p]) == {"a": ["s1"]}
