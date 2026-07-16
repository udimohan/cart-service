"""Tests for catalog_01637."""

import pytest

from cartservice.generated.catalog_01637 import (
    Product_01637,
    bucket_by_tag_01637,
    is_valid_sku_01637,
    price_with_tax_01637,
)


def test_price_with_tax_01637():
    assert price_with_tax_01637(1000, 500) == 1050


def test_price_with_tax_negative_01637():
    with pytest.raises(ValueError):
        price_with_tax_01637(1000, -1)


def test_is_valid_sku_01637():
    assert is_valid_sku_01637("abc123")
    assert not is_valid_sku_01637("")


def test_bucket_by_tag_01637():
    p = Product_01637("s1", 100, ["a"])
    assert bucket_by_tag_01637([p]) == {"a": ["s1"]}
