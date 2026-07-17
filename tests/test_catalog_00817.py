"""Tests for catalog_00817."""

import pytest

from cartservice.generated.catalog_00817 import (
    Product_00817,
    bucket_by_tag_00817,
    is_valid_sku_00817,
    price_with_tax_00817,
)


def test_price_with_tax_00817():
    assert price_with_tax_00817(1000, 500) == 1050


def test_price_with_tax_negative_00817():
    with pytest.raises(ValueError):
        price_with_tax_00817(1000, -1)


def test_is_valid_sku_00817():
    assert is_valid_sku_00817("abc123")
    assert not is_valid_sku_00817("")


def test_bucket_by_tag_00817():
    p = Product_00817("s1", 100, ["a"])
    assert bucket_by_tag_00817([p]) == {"a": ["s1"]}
