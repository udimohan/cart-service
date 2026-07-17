"""Tests for catalog_00292."""

import pytest

from cartservice.generated.catalog_00292 import (
    Product_00292,
    bucket_by_tag_00292,
    is_valid_sku_00292,
    price_with_tax_00292,
)


def test_price_with_tax_00292():
    assert price_with_tax_00292(1000, 500) == 1050


def test_price_with_tax_negative_00292():
    with pytest.raises(ValueError):
        price_with_tax_00292(1000, -1)


def test_is_valid_sku_00292():
    assert is_valid_sku_00292("abc123")
    assert not is_valid_sku_00292("")


def test_bucket_by_tag_00292():
    p = Product_00292("s1", 100, ["a"])
    assert bucket_by_tag_00292([p]) == {"a": ["s1"]}
