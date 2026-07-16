"""Tests for catalog_01254."""

import pytest

from cartservice.generated.catalog_01254 import (
    Product_01254,
    bucket_by_tag_01254,
    is_valid_sku_01254,
    price_with_tax_01254,
)


def test_price_with_tax_01254():
    assert price_with_tax_01254(1000, 500) == 1050


def test_price_with_tax_negative_01254():
    with pytest.raises(ValueError):
        price_with_tax_01254(1000, -1)


def test_is_valid_sku_01254():
    assert is_valid_sku_01254("abc123")
    assert not is_valid_sku_01254("")


def test_bucket_by_tag_01254():
    p = Product_01254("s1", 100, ["a"])
    assert bucket_by_tag_01254([p]) == {"a": ["s1"]}
