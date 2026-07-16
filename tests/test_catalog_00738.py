"""Tests for catalog_00738."""

import pytest

from cartservice.generated.catalog_00738 import (
    Product_00738,
    bucket_by_tag_00738,
    is_valid_sku_00738,
    price_with_tax_00738,
)


def test_price_with_tax_00738():
    assert price_with_tax_00738(1000, 500) == 1050


def test_price_with_tax_negative_00738():
    with pytest.raises(ValueError):
        price_with_tax_00738(1000, -1)


def test_is_valid_sku_00738():
    assert is_valid_sku_00738("abc123")
    assert not is_valid_sku_00738("")


def test_bucket_by_tag_00738():
    p = Product_00738("s1", 100, ["a"])
    assert bucket_by_tag_00738([p]) == {"a": ["s1"]}
