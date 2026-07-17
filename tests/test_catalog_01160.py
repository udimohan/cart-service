"""Tests for catalog_01160."""

import pytest

from cartservice.generated.catalog_01160 import (
    Product_01160,
    bucket_by_tag_01160,
    is_valid_sku_01160,
    price_with_tax_01160,
)


def test_price_with_tax_01160():
    assert price_with_tax_01160(1000, 500) == 1050


def test_price_with_tax_negative_01160():
    with pytest.raises(ValueError):
        price_with_tax_01160(1000, -1)


def test_is_valid_sku_01160():
    assert is_valid_sku_01160("abc123")
    assert not is_valid_sku_01160("")


def test_bucket_by_tag_01160():
    p = Product_01160("s1", 100, ["a"])
    assert bucket_by_tag_01160([p]) == {"a": ["s1"]}
