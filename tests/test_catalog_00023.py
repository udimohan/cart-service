"""Tests for catalog_00023."""

import pytest

from cartservice.generated.catalog_00023 import (
    Product_00023,
    bucket_by_tag_00023,
    is_valid_sku_00023,
    price_with_tax_00023,
)


def test_price_with_tax_00023():
    assert price_with_tax_00023(1000, 500) == 1050


def test_price_with_tax_negative_00023():
    with pytest.raises(ValueError):
        price_with_tax_00023(1000, -1)


def test_is_valid_sku_00023():
    assert is_valid_sku_00023("abc123")
    assert not is_valid_sku_00023("")


def test_bucket_by_tag_00023():
    p = Product_00023("s1", 100, ["a"])
    assert bucket_by_tag_00023([p]) == {"a": ["s1"]}
