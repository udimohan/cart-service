"""Tests for catalog_00657."""

import pytest

from cartservice.generated.catalog_00657 import (
    Product_00657,
    bucket_by_tag_00657,
    is_valid_sku_00657,
    price_with_tax_00657,
)


def test_price_with_tax_00657():
    assert price_with_tax_00657(1000, 500) == 1050


def test_price_with_tax_negative_00657():
    with pytest.raises(ValueError):
        price_with_tax_00657(1000, -1)


def test_is_valid_sku_00657():
    assert is_valid_sku_00657("abc123")
    assert not is_valid_sku_00657("")


def test_bucket_by_tag_00657():
    p = Product_00657("s1", 100, ["a"])
    assert bucket_by_tag_00657([p]) == {"a": ["s1"]}
