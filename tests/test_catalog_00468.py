"""Tests for catalog_00468."""

import pytest

from cartservice.generated.catalog_00468 import (
    Product_00468,
    bucket_by_tag_00468,
    is_valid_sku_00468,
    price_with_tax_00468,
)


def test_price_with_tax_00468():
    assert price_with_tax_00468(1000, 500) == 1050


def test_price_with_tax_negative_00468():
    with pytest.raises(ValueError):
        price_with_tax_00468(1000, -1)


def test_is_valid_sku_00468():
    assert is_valid_sku_00468("abc123")
    assert not is_valid_sku_00468("")


def test_bucket_by_tag_00468():
    p = Product_00468("s1", 100, ["a"])
    assert bucket_by_tag_00468([p]) == {"a": ["s1"]}
