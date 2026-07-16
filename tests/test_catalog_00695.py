"""Tests for catalog_00695."""

import pytest

from cartservice.generated.catalog_00695 import (
    Product_00695,
    bucket_by_tag_00695,
    is_valid_sku_00695,
    price_with_tax_00695,
)


def test_price_with_tax_00695():
    assert price_with_tax_00695(1000, 500) == 1050


def test_price_with_tax_negative_00695():
    with pytest.raises(ValueError):
        price_with_tax_00695(1000, -1)


def test_is_valid_sku_00695():
    assert is_valid_sku_00695("abc123")
    assert not is_valid_sku_00695("")


def test_bucket_by_tag_00695():
    p = Product_00695("s1", 100, ["a"])
    assert bucket_by_tag_00695([p]) == {"a": ["s1"]}
