"""Tests for catalog_00263."""

import pytest

from cartservice.generated.catalog_00263 import (
    Product_00263,
    bucket_by_tag_00263,
    is_valid_sku_00263,
    price_with_tax_00263,
)


def test_price_with_tax_00263():
    assert price_with_tax_00263(1000, 500) == 1050


def test_price_with_tax_negative_00263():
    with pytest.raises(ValueError):
        price_with_tax_00263(1000, -1)


def test_is_valid_sku_00263():
    assert is_valid_sku_00263("abc123")
    assert not is_valid_sku_00263("")


def test_bucket_by_tag_00263():
    p = Product_00263("s1", 100, ["a"])
    assert bucket_by_tag_00263([p]) == {"a": ["s1"]}
