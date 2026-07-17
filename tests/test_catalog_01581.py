"""Tests for catalog_01581."""

import pytest

from cartservice.generated.catalog_01581 import (
    Product_01581,
    bucket_by_tag_01581,
    is_valid_sku_01581,
    price_with_tax_01581,
)


def test_price_with_tax_01581():
    assert price_with_tax_01581(1000, 500) == 1050


def test_price_with_tax_negative_01581():
    with pytest.raises(ValueError):
        price_with_tax_01581(1000, -1)


def test_is_valid_sku_01581():
    assert is_valid_sku_01581("abc123")
    assert not is_valid_sku_01581("")


def test_bucket_by_tag_01581():
    p = Product_01581("s1", 100, ["a"])
    assert bucket_by_tag_01581([p]) == {"a": ["s1"]}
