"""Tests for catalog_00919."""

import pytest

from cartservice.generated.catalog_00919 import (
    Product_00919,
    bucket_by_tag_00919,
    is_valid_sku_00919,
    price_with_tax_00919,
)


def test_price_with_tax_00919():
    assert price_with_tax_00919(1000, 500) == 1050


def test_price_with_tax_negative_00919():
    with pytest.raises(ValueError):
        price_with_tax_00919(1000, -1)


def test_is_valid_sku_00919():
    assert is_valid_sku_00919("abc123")
    assert not is_valid_sku_00919("")


def test_bucket_by_tag_00919():
    p = Product_00919("s1", 100, ["a"])
    assert bucket_by_tag_00919([p]) == {"a": ["s1"]}
