"""Tests for catalog_00140."""

import pytest

from cartservice.generated.catalog_00140 import (
    Product_00140,
    bucket_by_tag_00140,
    is_valid_sku_00140,
    price_with_tax_00140,
)


def test_price_with_tax_00140():
    assert price_with_tax_00140(1000, 500) == 1050


def test_price_with_tax_negative_00140():
    with pytest.raises(ValueError):
        price_with_tax_00140(1000, -1)


def test_is_valid_sku_00140():
    assert is_valid_sku_00140("abc123")
    assert not is_valid_sku_00140("")


def test_bucket_by_tag_00140():
    p = Product_00140("s1", 100, ["a"])
    assert bucket_by_tag_00140([p]) == {"a": ["s1"]}
