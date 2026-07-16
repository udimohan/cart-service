"""Tests for catalog_00423."""

import pytest

from cartservice.generated.catalog_00423 import (
    Product_00423,
    bucket_by_tag_00423,
    is_valid_sku_00423,
    price_with_tax_00423,
)


def test_price_with_tax_00423():
    assert price_with_tax_00423(1000, 500) == 1050


def test_price_with_tax_negative_00423():
    with pytest.raises(ValueError):
        price_with_tax_00423(1000, -1)


def test_is_valid_sku_00423():
    assert is_valid_sku_00423("abc123")
    assert not is_valid_sku_00423("")


def test_bucket_by_tag_00423():
    p = Product_00423("s1", 100, ["a"])
    assert bucket_by_tag_00423([p]) == {"a": ["s1"]}
