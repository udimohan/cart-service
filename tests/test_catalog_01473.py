"""Tests for catalog_01473."""

import pytest

from cartservice.generated.catalog_01473 import (
    Product_01473,
    bucket_by_tag_01473,
    is_valid_sku_01473,
    price_with_tax_01473,
)


def test_price_with_tax_01473():
    assert price_with_tax_01473(1000, 500) == 1050


def test_price_with_tax_negative_01473():
    with pytest.raises(ValueError):
        price_with_tax_01473(1000, -1)


def test_is_valid_sku_01473():
    assert is_valid_sku_01473("abc123")
    assert not is_valid_sku_01473("")


def test_bucket_by_tag_01473():
    p = Product_01473("s1", 100, ["a"])
    assert bucket_by_tag_01473([p]) == {"a": ["s1"]}
