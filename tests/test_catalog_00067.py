"""Tests for catalog_00067."""

import pytest

from cartservice.generated.catalog_00067 import (
    Product_00067,
    bucket_by_tag_00067,
    is_valid_sku_00067,
    price_with_tax_00067,
)


def test_price_with_tax_00067():
    assert price_with_tax_00067(1000, 500) == 1050


def test_price_with_tax_negative_00067():
    with pytest.raises(ValueError):
        price_with_tax_00067(1000, -1)


def test_is_valid_sku_00067():
    assert is_valid_sku_00067("abc123")
    assert not is_valid_sku_00067("")


def test_bucket_by_tag_00067():
    p = Product_00067("s1", 100, ["a"])
    assert bucket_by_tag_00067([p]) == {"a": ["s1"]}
