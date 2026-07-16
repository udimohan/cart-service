"""Tests for catalog_01556."""

import pytest

from cartservice.generated.catalog_01556 import (
    Product_01556,
    bucket_by_tag_01556,
    is_valid_sku_01556,
    price_with_tax_01556,
)


def test_price_with_tax_01556():
    assert price_with_tax_01556(1000, 500) == 1050


def test_price_with_tax_negative_01556():
    with pytest.raises(ValueError):
        price_with_tax_01556(1000, -1)


def test_is_valid_sku_01556():
    assert is_valid_sku_01556("abc123")
    assert not is_valid_sku_01556("")


def test_bucket_by_tag_01556():
    p = Product_01556("s1", 100, ["a"])
    assert bucket_by_tag_01556([p]) == {"a": ["s1"]}
