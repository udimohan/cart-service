"""Tests for catalog_01661."""

import pytest

from cartservice.generated.catalog_01661 import (
    Product_01661,
    bucket_by_tag_01661,
    is_valid_sku_01661,
    price_with_tax_01661,
)


def test_price_with_tax_01661():
    assert price_with_tax_01661(1000, 500) == 1050


def test_price_with_tax_negative_01661():
    with pytest.raises(ValueError):
        price_with_tax_01661(1000, -1)


def test_is_valid_sku_01661():
    assert is_valid_sku_01661("abc123")
    assert not is_valid_sku_01661("")


def test_bucket_by_tag_01661():
    p = Product_01661("s1", 100, ["a"])
    assert bucket_by_tag_01661([p]) == {"a": ["s1"]}
