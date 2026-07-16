"""Tests for catalog_00354."""

import pytest

from cartservice.generated.catalog_00354 import (
    Product_00354,
    bucket_by_tag_00354,
    is_valid_sku_00354,
    price_with_tax_00354,
)


def test_price_with_tax_00354():
    assert price_with_tax_00354(1000, 500) == 1050


def test_price_with_tax_negative_00354():
    with pytest.raises(ValueError):
        price_with_tax_00354(1000, -1)


def test_is_valid_sku_00354():
    assert is_valid_sku_00354("abc123")
    assert not is_valid_sku_00354("")


def test_bucket_by_tag_00354():
    p = Product_00354("s1", 100, ["a"])
    assert bucket_by_tag_00354([p]) == {"a": ["s1"]}
