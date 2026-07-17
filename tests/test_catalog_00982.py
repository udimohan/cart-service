"""Tests for catalog_00982."""

import pytest

from cartservice.generated.catalog_00982 import (
    Product_00982,
    bucket_by_tag_00982,
    is_valid_sku_00982,
    price_with_tax_00982,
)


def test_price_with_tax_00982():
    assert price_with_tax_00982(1000, 500) == 1050


def test_price_with_tax_negative_00982():
    with pytest.raises(ValueError):
        price_with_tax_00982(1000, -1)


def test_is_valid_sku_00982():
    assert is_valid_sku_00982("abc123")
    assert not is_valid_sku_00982("")


def test_bucket_by_tag_00982():
    p = Product_00982("s1", 100, ["a"])
    assert bucket_by_tag_00982([p]) == {"a": ["s1"]}
