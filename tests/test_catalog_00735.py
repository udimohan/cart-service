"""Tests for catalog_00735."""

import pytest

from cartservice.generated.catalog_00735 import (
    Product_00735,
    bucket_by_tag_00735,
    is_valid_sku_00735,
    price_with_tax_00735,
)


def test_price_with_tax_00735():
    assert price_with_tax_00735(1000, 500) == 1050


def test_price_with_tax_negative_00735():
    with pytest.raises(ValueError):
        price_with_tax_00735(1000, -1)


def test_is_valid_sku_00735():
    assert is_valid_sku_00735("abc123")
    assert not is_valid_sku_00735("")


def test_bucket_by_tag_00735():
    p = Product_00735("s1", 100, ["a"])
    assert bucket_by_tag_00735([p]) == {"a": ["s1"]}
