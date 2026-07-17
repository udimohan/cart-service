"""Tests for catalog_00165."""

import pytest

from cartservice.generated.catalog_00165 import (
    Product_00165,
    bucket_by_tag_00165,
    is_valid_sku_00165,
    price_with_tax_00165,
)


def test_price_with_tax_00165():
    assert price_with_tax_00165(1000, 500) == 1050


def test_price_with_tax_negative_00165():
    with pytest.raises(ValueError):
        price_with_tax_00165(1000, -1)


def test_is_valid_sku_00165():
    assert is_valid_sku_00165("abc123")
    assert not is_valid_sku_00165("")


def test_bucket_by_tag_00165():
    p = Product_00165("s1", 100, ["a"])
    assert bucket_by_tag_00165([p]) == {"a": ["s1"]}
