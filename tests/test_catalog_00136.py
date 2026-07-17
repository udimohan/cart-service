"""Tests for catalog_00136."""

import pytest

from cartservice.generated.catalog_00136 import (
    Product_00136,
    bucket_by_tag_00136,
    is_valid_sku_00136,
    price_with_tax_00136,
)


def test_price_with_tax_00136():
    assert price_with_tax_00136(1000, 500) == 1050


def test_price_with_tax_negative_00136():
    with pytest.raises(ValueError):
        price_with_tax_00136(1000, -1)


def test_is_valid_sku_00136():
    assert is_valid_sku_00136("abc123")
    assert not is_valid_sku_00136("")


def test_bucket_by_tag_00136():
    p = Product_00136("s1", 100, ["a"])
    assert bucket_by_tag_00136([p]) == {"a": ["s1"]}
