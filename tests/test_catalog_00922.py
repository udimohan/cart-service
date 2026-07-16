"""Tests for catalog_00922."""

import pytest

from cartservice.generated.catalog_00922 import (
    Product_00922,
    bucket_by_tag_00922,
    is_valid_sku_00922,
    price_with_tax_00922,
)


def test_price_with_tax_00922():
    assert price_with_tax_00922(1000, 500) == 1050


def test_price_with_tax_negative_00922():
    with pytest.raises(ValueError):
        price_with_tax_00922(1000, -1)


def test_is_valid_sku_00922():
    assert is_valid_sku_00922("abc123")
    assert not is_valid_sku_00922("")


def test_bucket_by_tag_00922():
    p = Product_00922("s1", 100, ["a"])
    assert bucket_by_tag_00922([p]) == {"a": ["s1"]}
