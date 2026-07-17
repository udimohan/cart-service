"""Tests for catalog_00156."""

import pytest

from cartservice.generated.catalog_00156 import (
    Product_00156,
    bucket_by_tag_00156,
    is_valid_sku_00156,
    price_with_tax_00156,
)


def test_price_with_tax_00156():
    assert price_with_tax_00156(1000, 500) == 1050


def test_price_with_tax_negative_00156():
    with pytest.raises(ValueError):
        price_with_tax_00156(1000, -1)


def test_is_valid_sku_00156():
    assert is_valid_sku_00156("abc123")
    assert not is_valid_sku_00156("")


def test_bucket_by_tag_00156():
    p = Product_00156("s1", 100, ["a"])
    assert bucket_by_tag_00156([p]) == {"a": ["s1"]}
