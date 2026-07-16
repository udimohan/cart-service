"""Tests for catalog_00841."""

import pytest

from cartservice.generated.catalog_00841 import (
    Product_00841,
    bucket_by_tag_00841,
    is_valid_sku_00841,
    price_with_tax_00841,
)


def test_price_with_tax_00841():
    assert price_with_tax_00841(1000, 500) == 1050


def test_price_with_tax_negative_00841():
    with pytest.raises(ValueError):
        price_with_tax_00841(1000, -1)


def test_is_valid_sku_00841():
    assert is_valid_sku_00841("abc123")
    assert not is_valid_sku_00841("")


def test_bucket_by_tag_00841():
    p = Product_00841("s1", 100, ["a"])
    assert bucket_by_tag_00841([p]) == {"a": ["s1"]}
