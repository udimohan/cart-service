"""Tests for catalog_00469."""

import pytest

from cartservice.generated.catalog_00469 import (
    Product_00469,
    bucket_by_tag_00469,
    is_valid_sku_00469,
    price_with_tax_00469,
)


def test_price_with_tax_00469():
    assert price_with_tax_00469(1000, 500) == 1050


def test_price_with_tax_negative_00469():
    with pytest.raises(ValueError):
        price_with_tax_00469(1000, -1)


def test_is_valid_sku_00469():
    assert is_valid_sku_00469("abc123")
    assert not is_valid_sku_00469("")


def test_bucket_by_tag_00469():
    p = Product_00469("s1", 100, ["a"])
    assert bucket_by_tag_00469([p]) == {"a": ["s1"]}
