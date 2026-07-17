"""Tests for catalog_00044."""

import pytest

from cartservice.generated.catalog_00044 import (
    Product_00044,
    bucket_by_tag_00044,
    is_valid_sku_00044,
    price_with_tax_00044,
)


def test_price_with_tax_00044():
    assert price_with_tax_00044(1000, 500) == 1050


def test_price_with_tax_negative_00044():
    with pytest.raises(ValueError):
        price_with_tax_00044(1000, -1)


def test_is_valid_sku_00044():
    assert is_valid_sku_00044("abc123")
    assert not is_valid_sku_00044("")


def test_bucket_by_tag_00044():
    p = Product_00044("s1", 100, ["a"])
    assert bucket_by_tag_00044([p]) == {"a": ["s1"]}
