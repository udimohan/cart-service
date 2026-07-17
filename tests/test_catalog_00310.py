"""Tests for catalog_00310."""

import pytest

from cartservice.generated.catalog_00310 import (
    Product_00310,
    bucket_by_tag_00310,
    is_valid_sku_00310,
    price_with_tax_00310,
)


def test_price_with_tax_00310():
    assert price_with_tax_00310(1000, 500) == 1050


def test_price_with_tax_negative_00310():
    with pytest.raises(ValueError):
        price_with_tax_00310(1000, -1)


def test_is_valid_sku_00310():
    assert is_valid_sku_00310("abc123")
    assert not is_valid_sku_00310("")


def test_bucket_by_tag_00310():
    p = Product_00310("s1", 100, ["a"])
    assert bucket_by_tag_00310([p]) == {"a": ["s1"]}
