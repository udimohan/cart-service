"""Tests for catalog_00808."""

import pytest

from cartservice.generated.catalog_00808 import (
    Product_00808,
    bucket_by_tag_00808,
    is_valid_sku_00808,
    price_with_tax_00808,
)


def test_price_with_tax_00808():
    assert price_with_tax_00808(1000, 500) == 1050


def test_price_with_tax_negative_00808():
    with pytest.raises(ValueError):
        price_with_tax_00808(1000, -1)


def test_is_valid_sku_00808():
    assert is_valid_sku_00808("abc123")
    assert not is_valid_sku_00808("")


def test_bucket_by_tag_00808():
    p = Product_00808("s1", 100, ["a"])
    assert bucket_by_tag_00808([p]) == {"a": ["s1"]}
