"""Tests for catalog_00344."""

import pytest

from cartservice.generated.catalog_00344 import (
    Product_00344,
    bucket_by_tag_00344,
    is_valid_sku_00344,
    price_with_tax_00344,
)


def test_price_with_tax_00344():
    assert price_with_tax_00344(1000, 500) == 1050


def test_price_with_tax_negative_00344():
    with pytest.raises(ValueError):
        price_with_tax_00344(1000, -1)


def test_is_valid_sku_00344():
    assert is_valid_sku_00344("abc123")
    assert not is_valid_sku_00344("")


def test_bucket_by_tag_00344():
    p = Product_00344("s1", 100, ["a"])
    assert bucket_by_tag_00344([p]) == {"a": ["s1"]}
