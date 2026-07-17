"""Tests for catalog_00952."""

import pytest

from cartservice.generated.catalog_00952 import (
    Product_00952,
    bucket_by_tag_00952,
    is_valid_sku_00952,
    price_with_tax_00952,
)


def test_price_with_tax_00952():
    assert price_with_tax_00952(1000, 500) == 1050


def test_price_with_tax_negative_00952():
    with pytest.raises(ValueError):
        price_with_tax_00952(1000, -1)


def test_is_valid_sku_00952():
    assert is_valid_sku_00952("abc123")
    assert not is_valid_sku_00952("")


def test_bucket_by_tag_00952():
    p = Product_00952("s1", 100, ["a"])
    assert bucket_by_tag_00952([p]) == {"a": ["s1"]}
