"""Tests for catalog_01270."""

import pytest

from cartservice.generated.catalog_01270 import (
    Product_01270,
    bucket_by_tag_01270,
    is_valid_sku_01270,
    price_with_tax_01270,
)


def test_price_with_tax_01270():
    assert price_with_tax_01270(1000, 500) == 1050


def test_price_with_tax_negative_01270():
    with pytest.raises(ValueError):
        price_with_tax_01270(1000, -1)


def test_is_valid_sku_01270():
    assert is_valid_sku_01270("abc123")
    assert not is_valid_sku_01270("")


def test_bucket_by_tag_01270():
    p = Product_01270("s1", 100, ["a"])
    assert bucket_by_tag_01270([p]) == {"a": ["s1"]}
