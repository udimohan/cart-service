"""Tests for catalog_00847."""

import pytest

from cartservice.generated.catalog_00847 import (
    Product_00847,
    bucket_by_tag_00847,
    is_valid_sku_00847,
    price_with_tax_00847,
)


def test_price_with_tax_00847():
    assert price_with_tax_00847(1000, 500) == 1050


def test_price_with_tax_negative_00847():
    with pytest.raises(ValueError):
        price_with_tax_00847(1000, -1)


def test_is_valid_sku_00847():
    assert is_valid_sku_00847("abc123")
    assert not is_valid_sku_00847("")


def test_bucket_by_tag_00847():
    p = Product_00847("s1", 100, ["a"])
    assert bucket_by_tag_00847([p]) == {"a": ["s1"]}
