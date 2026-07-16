"""Tests for catalog_00279."""

import pytest

from cartservice.generated.catalog_00279 import (
    Product_00279,
    bucket_by_tag_00279,
    is_valid_sku_00279,
    price_with_tax_00279,
)


def test_price_with_tax_00279():
    assert price_with_tax_00279(1000, 500) == 1050


def test_price_with_tax_negative_00279():
    with pytest.raises(ValueError):
        price_with_tax_00279(1000, -1)


def test_is_valid_sku_00279():
    assert is_valid_sku_00279("abc123")
    assert not is_valid_sku_00279("")


def test_bucket_by_tag_00279():
    p = Product_00279("s1", 100, ["a"])
    assert bucket_by_tag_00279([p]) == {"a": ["s1"]}
