"""Tests for catalog_00262."""

import pytest

from cartservice.generated.catalog_00262 import (
    Product_00262,
    bucket_by_tag_00262,
    is_valid_sku_00262,
    price_with_tax_00262,
)


def test_price_with_tax_00262():
    assert price_with_tax_00262(1000, 500) == 1050


def test_price_with_tax_negative_00262():
    with pytest.raises(ValueError):
        price_with_tax_00262(1000, -1)


def test_is_valid_sku_00262():
    assert is_valid_sku_00262("abc123")
    assert not is_valid_sku_00262("")


def test_bucket_by_tag_00262():
    p = Product_00262("s1", 100, ["a"])
    assert bucket_by_tag_00262([p]) == {"a": ["s1"]}
