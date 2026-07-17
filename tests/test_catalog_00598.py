"""Tests for catalog_00598."""

import pytest

from cartservice.generated.catalog_00598 import (
    Product_00598,
    bucket_by_tag_00598,
    is_valid_sku_00598,
    price_with_tax_00598,
)


def test_price_with_tax_00598():
    assert price_with_tax_00598(1000, 500) == 1050


def test_price_with_tax_negative_00598():
    with pytest.raises(ValueError):
        price_with_tax_00598(1000, -1)


def test_is_valid_sku_00598():
    assert is_valid_sku_00598("abc123")
    assert not is_valid_sku_00598("")


def test_bucket_by_tag_00598():
    p = Product_00598("s1", 100, ["a"])
    assert bucket_by_tag_00598([p]) == {"a": ["s1"]}
