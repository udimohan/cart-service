"""Tests for catalog_01627."""

import pytest

from cartservice.generated.catalog_01627 import (
    Product_01627,
    bucket_by_tag_01627,
    is_valid_sku_01627,
    price_with_tax_01627,
)


def test_price_with_tax_01627():
    assert price_with_tax_01627(1000, 500) == 1050


def test_price_with_tax_negative_01627():
    with pytest.raises(ValueError):
        price_with_tax_01627(1000, -1)


def test_is_valid_sku_01627():
    assert is_valid_sku_01627("abc123")
    assert not is_valid_sku_01627("")


def test_bucket_by_tag_01627():
    p = Product_01627("s1", 100, ["a"])
    assert bucket_by_tag_01627([p]) == {"a": ["s1"]}
