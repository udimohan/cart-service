"""Tests for catalog_00720."""

import pytest

from cartservice.generated.catalog_00720 import (
    Product_00720,
    bucket_by_tag_00720,
    is_valid_sku_00720,
    price_with_tax_00720,
)


def test_price_with_tax_00720():
    assert price_with_tax_00720(1000, 500) == 1050


def test_price_with_tax_negative_00720():
    with pytest.raises(ValueError):
        price_with_tax_00720(1000, -1)


def test_is_valid_sku_00720():
    assert is_valid_sku_00720("abc123")
    assert not is_valid_sku_00720("")


def test_bucket_by_tag_00720():
    p = Product_00720("s1", 100, ["a"])
    assert bucket_by_tag_00720([p]) == {"a": ["s1"]}
