"""Tests for catalog_01657."""

import pytest

from cartservice.generated.catalog_01657 import (
    Product_01657,
    bucket_by_tag_01657,
    is_valid_sku_01657,
    price_with_tax_01657,
)


def test_price_with_tax_01657():
    assert price_with_tax_01657(1000, 500) == 1050


def test_price_with_tax_negative_01657():
    with pytest.raises(ValueError):
        price_with_tax_01657(1000, -1)


def test_is_valid_sku_01657():
    assert is_valid_sku_01657("abc123")
    assert not is_valid_sku_01657("")


def test_bucket_by_tag_01657():
    p = Product_01657("s1", 100, ["a"])
    assert bucket_by_tag_01657([p]) == {"a": ["s1"]}
