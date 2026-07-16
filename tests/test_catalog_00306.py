"""Tests for catalog_00306."""

import pytest

from cartservice.generated.catalog_00306 import (
    Product_00306,
    bucket_by_tag_00306,
    is_valid_sku_00306,
    price_with_tax_00306,
)


def test_price_with_tax_00306():
    assert price_with_tax_00306(1000, 500) == 1050


def test_price_with_tax_negative_00306():
    with pytest.raises(ValueError):
        price_with_tax_00306(1000, -1)


def test_is_valid_sku_00306():
    assert is_valid_sku_00306("abc123")
    assert not is_valid_sku_00306("")


def test_bucket_by_tag_00306():
    p = Product_00306("s1", 100, ["a"])
    assert bucket_by_tag_00306([p]) == {"a": ["s1"]}
