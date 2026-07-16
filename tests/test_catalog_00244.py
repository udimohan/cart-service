"""Tests for catalog_00244."""

import pytest

from cartservice.generated.catalog_00244 import (
    Product_00244,
    bucket_by_tag_00244,
    is_valid_sku_00244,
    price_with_tax_00244,
)


def test_price_with_tax_00244():
    assert price_with_tax_00244(1000, 500) == 1050


def test_price_with_tax_negative_00244():
    with pytest.raises(ValueError):
        price_with_tax_00244(1000, -1)


def test_is_valid_sku_00244():
    assert is_valid_sku_00244("abc123")
    assert not is_valid_sku_00244("")


def test_bucket_by_tag_00244():
    p = Product_00244("s1", 100, ["a"])
    assert bucket_by_tag_00244([p]) == {"a": ["s1"]}
