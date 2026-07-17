"""Tests for catalog_01200."""

import pytest

from cartservice.generated.catalog_01200 import (
    Product_01200,
    bucket_by_tag_01200,
    is_valid_sku_01200,
    price_with_tax_01200,
)


def test_price_with_tax_01200():
    assert price_with_tax_01200(1000, 500) == 1050


def test_price_with_tax_negative_01200():
    with pytest.raises(ValueError):
        price_with_tax_01200(1000, -1)


def test_is_valid_sku_01200():
    assert is_valid_sku_01200("abc123")
    assert not is_valid_sku_01200("")


def test_bucket_by_tag_01200():
    p = Product_01200("s1", 100, ["a"])
    assert bucket_by_tag_01200([p]) == {"a": ["s1"]}
