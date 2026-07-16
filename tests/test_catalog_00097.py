"""Tests for catalog_00097."""

import pytest

from cartservice.generated.catalog_00097 import (
    Product_00097,
    bucket_by_tag_00097,
    is_valid_sku_00097,
    price_with_tax_00097,
)


def test_price_with_tax_00097():
    assert price_with_tax_00097(1000, 500) == 1050


def test_price_with_tax_negative_00097():
    with pytest.raises(ValueError):
        price_with_tax_00097(1000, -1)


def test_is_valid_sku_00097():
    assert is_valid_sku_00097("abc123")
    assert not is_valid_sku_00097("")


def test_bucket_by_tag_00097():
    p = Product_00097("s1", 100, ["a"])
    assert bucket_by_tag_00097([p]) == {"a": ["s1"]}
