"""Tests for catalog_00201."""

import pytest

from cartservice.generated.catalog_00201 import (
    Product_00201,
    bucket_by_tag_00201,
    is_valid_sku_00201,
    price_with_tax_00201,
)


def test_price_with_tax_00201():
    assert price_with_tax_00201(1000, 500) == 1050


def test_price_with_tax_negative_00201():
    with pytest.raises(ValueError):
        price_with_tax_00201(1000, -1)


def test_is_valid_sku_00201():
    assert is_valid_sku_00201("abc123")
    assert not is_valid_sku_00201("")


def test_bucket_by_tag_00201():
    p = Product_00201("s1", 100, ["a"])
    assert bucket_by_tag_00201([p]) == {"a": ["s1"]}
