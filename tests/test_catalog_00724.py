"""Tests for catalog_00724."""

import pytest

from cartservice.generated.catalog_00724 import (
    Product_00724,
    bucket_by_tag_00724,
    is_valid_sku_00724,
    price_with_tax_00724,
)


def test_price_with_tax_00724():
    assert price_with_tax_00724(1000, 500) == 1050


def test_price_with_tax_negative_00724():
    with pytest.raises(ValueError):
        price_with_tax_00724(1000, -1)


def test_is_valid_sku_00724():
    assert is_valid_sku_00724("abc123")
    assert not is_valid_sku_00724("")


def test_bucket_by_tag_00724():
    p = Product_00724("s1", 100, ["a"])
    assert bucket_by_tag_00724([p]) == {"a": ["s1"]}
