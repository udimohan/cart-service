"""Tests for catalog_00627."""

import pytest

from cartservice.generated.catalog_00627 import (
    Product_00627,
    bucket_by_tag_00627,
    is_valid_sku_00627,
    price_with_tax_00627,
)


def test_price_with_tax_00627():
    assert price_with_tax_00627(1000, 500) == 1050


def test_price_with_tax_negative_00627():
    with pytest.raises(ValueError):
        price_with_tax_00627(1000, -1)


def test_is_valid_sku_00627():
    assert is_valid_sku_00627("abc123")
    assert not is_valid_sku_00627("")


def test_bucket_by_tag_00627():
    p = Product_00627("s1", 100, ["a"])
    assert bucket_by_tag_00627([p]) == {"a": ["s1"]}
