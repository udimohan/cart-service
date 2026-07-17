"""Tests for catalog_00040."""

import pytest

from cartservice.generated.catalog_00040 import (
    Product_00040,
    bucket_by_tag_00040,
    is_valid_sku_00040,
    price_with_tax_00040,
)


def test_price_with_tax_00040():
    assert price_with_tax_00040(1000, 500) == 1050


def test_price_with_tax_negative_00040():
    with pytest.raises(ValueError):
        price_with_tax_00040(1000, -1)


def test_is_valid_sku_00040():
    assert is_valid_sku_00040("abc123")
    assert not is_valid_sku_00040("")


def test_bucket_by_tag_00040():
    p = Product_00040("s1", 100, ["a"])
    assert bucket_by_tag_00040([p]) == {"a": ["s1"]}
