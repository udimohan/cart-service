"""Tests for catalog_01097."""

import pytest

from cartservice.generated.catalog_01097 import (
    Product_01097,
    bucket_by_tag_01097,
    is_valid_sku_01097,
    price_with_tax_01097,
)


def test_price_with_tax_01097():
    assert price_with_tax_01097(1000, 500) == 1050


def test_price_with_tax_negative_01097():
    with pytest.raises(ValueError):
        price_with_tax_01097(1000, -1)


def test_is_valid_sku_01097():
    assert is_valid_sku_01097("abc123")
    assert not is_valid_sku_01097("")


def test_bucket_by_tag_01097():
    p = Product_01097("s1", 100, ["a"])
    assert bucket_by_tag_01097([p]) == {"a": ["s1"]}
