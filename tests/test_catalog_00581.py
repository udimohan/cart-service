"""Tests for catalog_00581."""

import pytest

from cartservice.generated.catalog_00581 import (
    Product_00581,
    bucket_by_tag_00581,
    is_valid_sku_00581,
    price_with_tax_00581,
)


def test_price_with_tax_00581():
    assert price_with_tax_00581(1000, 500) == 1050


def test_price_with_tax_negative_00581():
    with pytest.raises(ValueError):
        price_with_tax_00581(1000, -1)


def test_is_valid_sku_00581():
    assert is_valid_sku_00581("abc123")
    assert not is_valid_sku_00581("")


def test_bucket_by_tag_00581():
    p = Product_00581("s1", 100, ["a"])
    assert bucket_by_tag_00581([p]) == {"a": ["s1"]}
