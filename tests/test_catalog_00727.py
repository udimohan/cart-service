"""Tests for catalog_00727."""

import pytest

from cartservice.generated.catalog_00727 import (
    Product_00727,
    bucket_by_tag_00727,
    is_valid_sku_00727,
    price_with_tax_00727,
)


def test_price_with_tax_00727():
    assert price_with_tax_00727(1000, 500) == 1050


def test_price_with_tax_negative_00727():
    with pytest.raises(ValueError):
        price_with_tax_00727(1000, -1)


def test_is_valid_sku_00727():
    assert is_valid_sku_00727("abc123")
    assert not is_valid_sku_00727("")


def test_bucket_by_tag_00727():
    p = Product_00727("s1", 100, ["a"])
    assert bucket_by_tag_00727([p]) == {"a": ["s1"]}
