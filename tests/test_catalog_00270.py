"""Tests for catalog_00270."""

import pytest

from cartservice.generated.catalog_00270 import (
    Product_00270,
    bucket_by_tag_00270,
    is_valid_sku_00270,
    price_with_tax_00270,
)


def test_price_with_tax_00270():
    assert price_with_tax_00270(1000, 500) == 1050


def test_price_with_tax_negative_00270():
    with pytest.raises(ValueError):
        price_with_tax_00270(1000, -1)


def test_is_valid_sku_00270():
    assert is_valid_sku_00270("abc123")
    assert not is_valid_sku_00270("")


def test_bucket_by_tag_00270():
    p = Product_00270("s1", 100, ["a"])
    assert bucket_by_tag_00270([p]) == {"a": ["s1"]}
