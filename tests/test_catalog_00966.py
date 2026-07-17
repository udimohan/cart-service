"""Tests for catalog_00966."""

import pytest

from cartservice.generated.catalog_00966 import (
    Product_00966,
    bucket_by_tag_00966,
    is_valid_sku_00966,
    price_with_tax_00966,
)


def test_price_with_tax_00966():
    assert price_with_tax_00966(1000, 500) == 1050


def test_price_with_tax_negative_00966():
    with pytest.raises(ValueError):
        price_with_tax_00966(1000, -1)


def test_is_valid_sku_00966():
    assert is_valid_sku_00966("abc123")
    assert not is_valid_sku_00966("")


def test_bucket_by_tag_00966():
    p = Product_00966("s1", 100, ["a"])
    assert bucket_by_tag_00966([p]) == {"a": ["s1"]}
