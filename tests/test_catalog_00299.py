"""Tests for catalog_00299."""

import pytest

from cartservice.generated.catalog_00299 import (
    Product_00299,
    bucket_by_tag_00299,
    is_valid_sku_00299,
    price_with_tax_00299,
)


def test_price_with_tax_00299():
    assert price_with_tax_00299(1000, 500) == 1050


def test_price_with_tax_negative_00299():
    with pytest.raises(ValueError):
        price_with_tax_00299(1000, -1)


def test_is_valid_sku_00299():
    assert is_valid_sku_00299("abc123")
    assert not is_valid_sku_00299("")


def test_bucket_by_tag_00299():
    p = Product_00299("s1", 100, ["a"])
    assert bucket_by_tag_00299([p]) == {"a": ["s1"]}
