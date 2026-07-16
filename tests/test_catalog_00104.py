"""Tests for catalog_00104."""

import pytest

from cartservice.generated.catalog_00104 import (
    Product_00104,
    bucket_by_tag_00104,
    is_valid_sku_00104,
    price_with_tax_00104,
)


def test_price_with_tax_00104():
    assert price_with_tax_00104(1000, 500) == 1050


def test_price_with_tax_negative_00104():
    with pytest.raises(ValueError):
        price_with_tax_00104(1000, -1)


def test_is_valid_sku_00104():
    assert is_valid_sku_00104("abc123")
    assert not is_valid_sku_00104("")


def test_bucket_by_tag_00104():
    p = Product_00104("s1", 100, ["a"])
    assert bucket_by_tag_00104([p]) == {"a": ["s1"]}
