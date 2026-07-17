"""Tests for catalog_01643."""

import pytest

from cartservice.generated.catalog_01643 import (
    Product_01643,
    bucket_by_tag_01643,
    is_valid_sku_01643,
    price_with_tax_01643,
)


def test_price_with_tax_01643():
    assert price_with_tax_01643(1000, 500) == 1050


def test_price_with_tax_negative_01643():
    with pytest.raises(ValueError):
        price_with_tax_01643(1000, -1)


def test_is_valid_sku_01643():
    assert is_valid_sku_01643("abc123")
    assert not is_valid_sku_01643("")


def test_bucket_by_tag_01643():
    p = Product_01643("s1", 100, ["a"])
    assert bucket_by_tag_01643([p]) == {"a": ["s1"]}
