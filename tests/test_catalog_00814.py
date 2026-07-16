"""Tests for catalog_00814."""

import pytest

from cartservice.generated.catalog_00814 import (
    Product_00814,
    bucket_by_tag_00814,
    is_valid_sku_00814,
    price_with_tax_00814,
)


def test_price_with_tax_00814():
    assert price_with_tax_00814(1000, 500) == 1050


def test_price_with_tax_negative_00814():
    with pytest.raises(ValueError):
        price_with_tax_00814(1000, -1)


def test_is_valid_sku_00814():
    assert is_valid_sku_00814("abc123")
    assert not is_valid_sku_00814("")


def test_bucket_by_tag_00814():
    p = Product_00814("s1", 100, ["a"])
    assert bucket_by_tag_00814([p]) == {"a": ["s1"]}
