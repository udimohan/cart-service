"""Tests for catalog_01622."""

import pytest

from cartservice.generated.catalog_01622 import (
    Product_01622,
    bucket_by_tag_01622,
    is_valid_sku_01622,
    price_with_tax_01622,
)


def test_price_with_tax_01622():
    assert price_with_tax_01622(1000, 500) == 1050


def test_price_with_tax_negative_01622():
    with pytest.raises(ValueError):
        price_with_tax_01622(1000, -1)


def test_is_valid_sku_01622():
    assert is_valid_sku_01622("abc123")
    assert not is_valid_sku_01622("")


def test_bucket_by_tag_01622():
    p = Product_01622("s1", 100, ["a"])
    assert bucket_by_tag_01622([p]) == {"a": ["s1"]}
