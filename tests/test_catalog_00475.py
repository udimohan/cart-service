"""Tests for catalog_00475."""

import pytest

from cartservice.generated.catalog_00475 import (
    Product_00475,
    bucket_by_tag_00475,
    is_valid_sku_00475,
    price_with_tax_00475,
)


def test_price_with_tax_00475():
    assert price_with_tax_00475(1000, 500) == 1050


def test_price_with_tax_negative_00475():
    with pytest.raises(ValueError):
        price_with_tax_00475(1000, -1)


def test_is_valid_sku_00475():
    assert is_valid_sku_00475("abc123")
    assert not is_valid_sku_00475("")


def test_bucket_by_tag_00475():
    p = Product_00475("s1", 100, ["a"])
    assert bucket_by_tag_00475([p]) == {"a": ["s1"]}
