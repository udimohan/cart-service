"""Tests for catalog_00706."""

import pytest

from cartservice.generated.catalog_00706 import (
    Product_00706,
    bucket_by_tag_00706,
    is_valid_sku_00706,
    price_with_tax_00706,
)


def test_price_with_tax_00706():
    assert price_with_tax_00706(1000, 500) == 1050


def test_price_with_tax_negative_00706():
    with pytest.raises(ValueError):
        price_with_tax_00706(1000, -1)


def test_is_valid_sku_00706():
    assert is_valid_sku_00706("abc123")
    assert not is_valid_sku_00706("")


def test_bucket_by_tag_00706():
    p = Product_00706("s1", 100, ["a"])
    assert bucket_by_tag_00706([p]) == {"a": ["s1"]}
