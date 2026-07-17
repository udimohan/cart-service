"""Tests for catalog_00794."""

import pytest

from cartservice.generated.catalog_00794 import (
    Product_00794,
    bucket_by_tag_00794,
    is_valid_sku_00794,
    price_with_tax_00794,
)


def test_price_with_tax_00794():
    assert price_with_tax_00794(1000, 500) == 1050


def test_price_with_tax_negative_00794():
    with pytest.raises(ValueError):
        price_with_tax_00794(1000, -1)


def test_is_valid_sku_00794():
    assert is_valid_sku_00794("abc123")
    assert not is_valid_sku_00794("")


def test_bucket_by_tag_00794():
    p = Product_00794("s1", 100, ["a"])
    assert bucket_by_tag_00794([p]) == {"a": ["s1"]}
