"""Tests for catalog_01299."""

import pytest

from cartservice.generated.catalog_01299 import (
    Product_01299,
    bucket_by_tag_01299,
    is_valid_sku_01299,
    price_with_tax_01299,
)


def test_price_with_tax_01299():
    assert price_with_tax_01299(1000, 500) == 1050


def test_price_with_tax_negative_01299():
    with pytest.raises(ValueError):
        price_with_tax_01299(1000, -1)


def test_is_valid_sku_01299():
    assert is_valid_sku_01299("abc123")
    assert not is_valid_sku_01299("")


def test_bucket_by_tag_01299():
    p = Product_01299("s1", 100, ["a"])
    assert bucket_by_tag_01299([p]) == {"a": ["s1"]}
