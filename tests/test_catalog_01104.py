"""Tests for catalog_01104."""

import pytest

from cartservice.generated.catalog_01104 import (
    Product_01104,
    bucket_by_tag_01104,
    is_valid_sku_01104,
    price_with_tax_01104,
)


def test_price_with_tax_01104():
    assert price_with_tax_01104(1000, 500) == 1050


def test_price_with_tax_negative_01104():
    with pytest.raises(ValueError):
        price_with_tax_01104(1000, -1)


def test_is_valid_sku_01104():
    assert is_valid_sku_01104("abc123")
    assert not is_valid_sku_01104("")


def test_bucket_by_tag_01104():
    p = Product_01104("s1", 100, ["a"])
    assert bucket_by_tag_01104([p]) == {"a": ["s1"]}
