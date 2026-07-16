"""Tests for catalog_00415."""

import pytest

from cartservice.generated.catalog_00415 import (
    Product_00415,
    bucket_by_tag_00415,
    is_valid_sku_00415,
    price_with_tax_00415,
)


def test_price_with_tax_00415():
    assert price_with_tax_00415(1000, 500) == 1050


def test_price_with_tax_negative_00415():
    with pytest.raises(ValueError):
        price_with_tax_00415(1000, -1)


def test_is_valid_sku_00415():
    assert is_valid_sku_00415("abc123")
    assert not is_valid_sku_00415("")


def test_bucket_by_tag_00415():
    p = Product_00415("s1", 100, ["a"])
    assert bucket_by_tag_00415([p]) == {"a": ["s1"]}
