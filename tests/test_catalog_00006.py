"""Tests for catalog_00006."""

import pytest

from cartservice.generated.catalog_00006 import (
    Product_00006,
    bucket_by_tag_00006,
    is_valid_sku_00006,
    price_with_tax_00006,
)


def test_price_with_tax_00006():
    assert price_with_tax_00006(1000, 500) == 1050


def test_price_with_tax_negative_00006():
    with pytest.raises(ValueError):
        price_with_tax_00006(1000, -1)


def test_is_valid_sku_00006():
    assert is_valid_sku_00006("abc123")
    assert not is_valid_sku_00006("")


def test_bucket_by_tag_00006():
    p = Product_00006("s1", 100, ["a"])
    assert bucket_by_tag_00006([p]) == {"a": ["s1"]}
