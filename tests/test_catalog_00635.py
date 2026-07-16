"""Tests for catalog_00635."""

import pytest

from cartservice.generated.catalog_00635 import (
    Product_00635,
    bucket_by_tag_00635,
    is_valid_sku_00635,
    price_with_tax_00635,
)


def test_price_with_tax_00635():
    assert price_with_tax_00635(1000, 500) == 1050


def test_price_with_tax_negative_00635():
    with pytest.raises(ValueError):
        price_with_tax_00635(1000, -1)


def test_is_valid_sku_00635():
    assert is_valid_sku_00635("abc123")
    assert not is_valid_sku_00635("")


def test_bucket_by_tag_00635():
    p = Product_00635("s1", 100, ["a"])
    assert bucket_by_tag_00635([p]) == {"a": ["s1"]}
