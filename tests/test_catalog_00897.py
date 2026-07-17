"""Tests for catalog_00897."""

import pytest

from cartservice.generated.catalog_00897 import (
    Product_00897,
    bucket_by_tag_00897,
    is_valid_sku_00897,
    price_with_tax_00897,
)


def test_price_with_tax_00897():
    assert price_with_tax_00897(1000, 500) == 1050


def test_price_with_tax_negative_00897():
    with pytest.raises(ValueError):
        price_with_tax_00897(1000, -1)


def test_is_valid_sku_00897():
    assert is_valid_sku_00897("abc123")
    assert not is_valid_sku_00897("")


def test_bucket_by_tag_00897():
    p = Product_00897("s1", 100, ["a"])
    assert bucket_by_tag_00897([p]) == {"a": ["s1"]}
