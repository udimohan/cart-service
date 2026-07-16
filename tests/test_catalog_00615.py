"""Tests for catalog_00615."""

import pytest

from cartservice.generated.catalog_00615 import (
    Product_00615,
    bucket_by_tag_00615,
    is_valid_sku_00615,
    price_with_tax_00615,
)


def test_price_with_tax_00615():
    assert price_with_tax_00615(1000, 500) == 1050


def test_price_with_tax_negative_00615():
    with pytest.raises(ValueError):
        price_with_tax_00615(1000, -1)


def test_is_valid_sku_00615():
    assert is_valid_sku_00615("abc123")
    assert not is_valid_sku_00615("")


def test_bucket_by_tag_00615():
    p = Product_00615("s1", 100, ["a"])
    assert bucket_by_tag_00615([p]) == {"a": ["s1"]}
