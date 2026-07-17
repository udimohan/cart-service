"""Tests for catalog_00931."""

import pytest

from cartservice.generated.catalog_00931 import (
    Product_00931,
    bucket_by_tag_00931,
    is_valid_sku_00931,
    price_with_tax_00931,
)


def test_price_with_tax_00931():
    assert price_with_tax_00931(1000, 500) == 1050


def test_price_with_tax_negative_00931():
    with pytest.raises(ValueError):
        price_with_tax_00931(1000, -1)


def test_is_valid_sku_00931():
    assert is_valid_sku_00931("abc123")
    assert not is_valid_sku_00931("")


def test_bucket_by_tag_00931():
    p = Product_00931("s1", 100, ["a"])
    assert bucket_by_tag_00931([p]) == {"a": ["s1"]}
