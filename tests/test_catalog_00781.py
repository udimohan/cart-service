"""Tests for catalog_00781."""

import pytest

from cartservice.generated.catalog_00781 import (
    Product_00781,
    bucket_by_tag_00781,
    is_valid_sku_00781,
    price_with_tax_00781,
)


def test_price_with_tax_00781():
    assert price_with_tax_00781(1000, 500) == 1050


def test_price_with_tax_negative_00781():
    with pytest.raises(ValueError):
        price_with_tax_00781(1000, -1)


def test_is_valid_sku_00781():
    assert is_valid_sku_00781("abc123")
    assert not is_valid_sku_00781("")


def test_bucket_by_tag_00781():
    p = Product_00781("s1", 100, ["a"])
    assert bucket_by_tag_00781([p]) == {"a": ["s1"]}
