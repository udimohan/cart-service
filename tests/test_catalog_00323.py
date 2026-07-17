"""Tests for catalog_00323."""

import pytest

from cartservice.generated.catalog_00323 import (
    Product_00323,
    bucket_by_tag_00323,
    is_valid_sku_00323,
    price_with_tax_00323,
)


def test_price_with_tax_00323():
    assert price_with_tax_00323(1000, 500) == 1050


def test_price_with_tax_negative_00323():
    with pytest.raises(ValueError):
        price_with_tax_00323(1000, -1)


def test_is_valid_sku_00323():
    assert is_valid_sku_00323("abc123")
    assert not is_valid_sku_00323("")


def test_bucket_by_tag_00323():
    p = Product_00323("s1", 100, ["a"])
    assert bucket_by_tag_00323([p]) == {"a": ["s1"]}
