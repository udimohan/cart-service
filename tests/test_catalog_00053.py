"""Tests for catalog_00053."""

import pytest

from cartservice.generated.catalog_00053 import (
    Product_00053,
    bucket_by_tag_00053,
    is_valid_sku_00053,
    price_with_tax_00053,
)


def test_price_with_tax_00053():
    assert price_with_tax_00053(1000, 500) == 1050


def test_price_with_tax_negative_00053():
    with pytest.raises(ValueError):
        price_with_tax_00053(1000, -1)


def test_is_valid_sku_00053():
    assert is_valid_sku_00053("abc123")
    assert not is_valid_sku_00053("")


def test_bucket_by_tag_00053():
    p = Product_00053("s1", 100, ["a"])
    assert bucket_by_tag_00053([p]) == {"a": ["s1"]}
