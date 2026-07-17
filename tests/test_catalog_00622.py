"""Tests for catalog_00622."""

import pytest

from cartservice.generated.catalog_00622 import (
    Product_00622,
    bucket_by_tag_00622,
    is_valid_sku_00622,
    price_with_tax_00622,
)


def test_price_with_tax_00622():
    assert price_with_tax_00622(1000, 500) == 1050


def test_price_with_tax_negative_00622():
    with pytest.raises(ValueError):
        price_with_tax_00622(1000, -1)


def test_is_valid_sku_00622():
    assert is_valid_sku_00622("abc123")
    assert not is_valid_sku_00622("")


def test_bucket_by_tag_00622():
    p = Product_00622("s1", 100, ["a"])
    assert bucket_by_tag_00622([p]) == {"a": ["s1"]}
