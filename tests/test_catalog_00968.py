"""Tests for catalog_00968."""

import pytest

from cartservice.generated.catalog_00968 import (
    Product_00968,
    bucket_by_tag_00968,
    is_valid_sku_00968,
    price_with_tax_00968,
)


def test_price_with_tax_00968():
    assert price_with_tax_00968(1000, 500) == 1050


def test_price_with_tax_negative_00968():
    with pytest.raises(ValueError):
        price_with_tax_00968(1000, -1)


def test_is_valid_sku_00968():
    assert is_valid_sku_00968("abc123")
    assert not is_valid_sku_00968("")


def test_bucket_by_tag_00968():
    p = Product_00968("s1", 100, ["a"])
    assert bucket_by_tag_00968([p]) == {"a": ["s1"]}
