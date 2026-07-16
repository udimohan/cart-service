"""Tests for catalog_00921."""

import pytest

from cartservice.generated.catalog_00921 import (
    Product_00921,
    bucket_by_tag_00921,
    is_valid_sku_00921,
    price_with_tax_00921,
)


def test_price_with_tax_00921():
    assert price_with_tax_00921(1000, 500) == 1050


def test_price_with_tax_negative_00921():
    with pytest.raises(ValueError):
        price_with_tax_00921(1000, -1)


def test_is_valid_sku_00921():
    assert is_valid_sku_00921("abc123")
    assert not is_valid_sku_00921("")


def test_bucket_by_tag_00921():
    p = Product_00921("s1", 100, ["a"])
    assert bucket_by_tag_00921([p]) == {"a": ["s1"]}
