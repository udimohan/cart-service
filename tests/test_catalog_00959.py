"""Tests for catalog_00959."""

import pytest

from cartservice.generated.catalog_00959 import (
    Product_00959,
    bucket_by_tag_00959,
    is_valid_sku_00959,
    price_with_tax_00959,
)


def test_price_with_tax_00959():
    assert price_with_tax_00959(1000, 500) == 1050


def test_price_with_tax_negative_00959():
    with pytest.raises(ValueError):
        price_with_tax_00959(1000, -1)


def test_is_valid_sku_00959():
    assert is_valid_sku_00959("abc123")
    assert not is_valid_sku_00959("")


def test_bucket_by_tag_00959():
    p = Product_00959("s1", 100, ["a"])
    assert bucket_by_tag_00959([p]) == {"a": ["s1"]}
