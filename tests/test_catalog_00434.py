"""Tests for catalog_00434."""

import pytest

from cartservice.generated.catalog_00434 import (
    Product_00434,
    bucket_by_tag_00434,
    is_valid_sku_00434,
    price_with_tax_00434,
)


def test_price_with_tax_00434():
    assert price_with_tax_00434(1000, 500) == 1050


def test_price_with_tax_negative_00434():
    with pytest.raises(ValueError):
        price_with_tax_00434(1000, -1)


def test_is_valid_sku_00434():
    assert is_valid_sku_00434("abc123")
    assert not is_valid_sku_00434("")


def test_bucket_by_tag_00434():
    p = Product_00434("s1", 100, ["a"])
    assert bucket_by_tag_00434([p]) == {"a": ["s1"]}
