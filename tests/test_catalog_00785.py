"""Tests for catalog_00785."""

import pytest

from cartservice.generated.catalog_00785 import (
    Product_00785,
    bucket_by_tag_00785,
    is_valid_sku_00785,
    price_with_tax_00785,
)


def test_price_with_tax_00785():
    assert price_with_tax_00785(1000, 500) == 1050


def test_price_with_tax_negative_00785():
    with pytest.raises(ValueError):
        price_with_tax_00785(1000, -1)


def test_is_valid_sku_00785():
    assert is_valid_sku_00785("abc123")
    assert not is_valid_sku_00785("")


def test_bucket_by_tag_00785():
    p = Product_00785("s1", 100, ["a"])
    assert bucket_by_tag_00785([p]) == {"a": ["s1"]}
