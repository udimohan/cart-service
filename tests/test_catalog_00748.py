"""Tests for catalog_00748."""

import pytest

from cartservice.generated.catalog_00748 import (
    Product_00748,
    bucket_by_tag_00748,
    is_valid_sku_00748,
    price_with_tax_00748,
)


def test_price_with_tax_00748():
    assert price_with_tax_00748(1000, 500) == 1050


def test_price_with_tax_negative_00748():
    with pytest.raises(ValueError):
        price_with_tax_00748(1000, -1)


def test_is_valid_sku_00748():
    assert is_valid_sku_00748("abc123")
    assert not is_valid_sku_00748("")


def test_bucket_by_tag_00748():
    p = Product_00748("s1", 100, ["a"])
    assert bucket_by_tag_00748([p]) == {"a": ["s1"]}
