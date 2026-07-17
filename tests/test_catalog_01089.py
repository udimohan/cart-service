"""Tests for catalog_01089."""

import pytest

from cartservice.generated.catalog_01089 import (
    Product_01089,
    bucket_by_tag_01089,
    is_valid_sku_01089,
    price_with_tax_01089,
)


def test_price_with_tax_01089():
    assert price_with_tax_01089(1000, 500) == 1050


def test_price_with_tax_negative_01089():
    with pytest.raises(ValueError):
        price_with_tax_01089(1000, -1)


def test_is_valid_sku_01089():
    assert is_valid_sku_01089("abc123")
    assert not is_valid_sku_01089("")


def test_bucket_by_tag_01089():
    p = Product_01089("s1", 100, ["a"])
    assert bucket_by_tag_01089([p]) == {"a": ["s1"]}
