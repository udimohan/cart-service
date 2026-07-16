"""Tests for catalog_00373."""

import pytest

from cartservice.generated.catalog_00373 import (
    Product_00373,
    bucket_by_tag_00373,
    is_valid_sku_00373,
    price_with_tax_00373,
)


def test_price_with_tax_00373():
    assert price_with_tax_00373(1000, 500) == 1050


def test_price_with_tax_negative_00373():
    with pytest.raises(ValueError):
        price_with_tax_00373(1000, -1)


def test_is_valid_sku_00373():
    assert is_valid_sku_00373("abc123")
    assert not is_valid_sku_00373("")


def test_bucket_by_tag_00373():
    p = Product_00373("s1", 100, ["a"])
    assert bucket_by_tag_00373([p]) == {"a": ["s1"]}
