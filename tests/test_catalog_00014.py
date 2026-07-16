"""Tests for catalog_00014."""

import pytest

from cartservice.generated.catalog_00014 import (
    Product_00014,
    bucket_by_tag_00014,
    is_valid_sku_00014,
    price_with_tax_00014,
)


def test_price_with_tax_00014():
    assert price_with_tax_00014(1000, 500) == 1050


def test_price_with_tax_negative_00014():
    with pytest.raises(ValueError):
        price_with_tax_00014(1000, -1)


def test_is_valid_sku_00014():
    assert is_valid_sku_00014("abc123")
    assert not is_valid_sku_00014("")


def test_bucket_by_tag_00014():
    p = Product_00014("s1", 100, ["a"])
    assert bucket_by_tag_00014([p]) == {"a": ["s1"]}
