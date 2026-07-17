"""Tests for catalog_00711."""

import pytest

from cartservice.generated.catalog_00711 import (
    Product_00711,
    bucket_by_tag_00711,
    is_valid_sku_00711,
    price_with_tax_00711,
)


def test_price_with_tax_00711():
    assert price_with_tax_00711(1000, 500) == 1050


def test_price_with_tax_negative_00711():
    with pytest.raises(ValueError):
        price_with_tax_00711(1000, -1)


def test_is_valid_sku_00711():
    assert is_valid_sku_00711("abc123")
    assert not is_valid_sku_00711("")


def test_bucket_by_tag_00711():
    p = Product_00711("s1", 100, ["a"])
    assert bucket_by_tag_00711([p]) == {"a": ["s1"]}
