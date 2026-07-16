"""Tests for catalog_00327."""

import pytest

from cartservice.generated.catalog_00327 import (
    Product_00327,
    bucket_by_tag_00327,
    is_valid_sku_00327,
    price_with_tax_00327,
)


def test_price_with_tax_00327():
    assert price_with_tax_00327(1000, 500) == 1050


def test_price_with_tax_negative_00327():
    with pytest.raises(ValueError):
        price_with_tax_00327(1000, -1)


def test_is_valid_sku_00327():
    assert is_valid_sku_00327("abc123")
    assert not is_valid_sku_00327("")


def test_bucket_by_tag_00327():
    p = Product_00327("s1", 100, ["a"])
    assert bucket_by_tag_00327([p]) == {"a": ["s1"]}
