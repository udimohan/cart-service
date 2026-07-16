"""Tests for catalog_01345."""

import pytest

from cartservice.generated.catalog_01345 import (
    Product_01345,
    bucket_by_tag_01345,
    is_valid_sku_01345,
    price_with_tax_01345,
)


def test_price_with_tax_01345():
    assert price_with_tax_01345(1000, 500) == 1050


def test_price_with_tax_negative_01345():
    with pytest.raises(ValueError):
        price_with_tax_01345(1000, -1)


def test_is_valid_sku_01345():
    assert is_valid_sku_01345("abc123")
    assert not is_valid_sku_01345("")


def test_bucket_by_tag_01345():
    p = Product_01345("s1", 100, ["a"])
    assert bucket_by_tag_01345([p]) == {"a": ["s1"]}
