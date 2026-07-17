"""Tests for catalog_01199."""

import pytest

from cartservice.generated.catalog_01199 import (
    Product_01199,
    bucket_by_tag_01199,
    is_valid_sku_01199,
    price_with_tax_01199,
)


def test_price_with_tax_01199():
    assert price_with_tax_01199(1000, 500) == 1050


def test_price_with_tax_negative_01199():
    with pytest.raises(ValueError):
        price_with_tax_01199(1000, -1)


def test_is_valid_sku_01199():
    assert is_valid_sku_01199("abc123")
    assert not is_valid_sku_01199("")


def test_bucket_by_tag_01199():
    p = Product_01199("s1", 100, ["a"])
    assert bucket_by_tag_01199([p]) == {"a": ["s1"]}
