"""Tests for catalog_00105."""

import pytest

from cartservice.generated.catalog_00105 import (
    Product_00105,
    bucket_by_tag_00105,
    is_valid_sku_00105,
    price_with_tax_00105,
)


def test_price_with_tax_00105():
    assert price_with_tax_00105(1000, 500) == 1050


def test_price_with_tax_negative_00105():
    with pytest.raises(ValueError):
        price_with_tax_00105(1000, -1)


def test_is_valid_sku_00105():
    assert is_valid_sku_00105("abc123")
    assert not is_valid_sku_00105("")


def test_bucket_by_tag_00105():
    p = Product_00105("s1", 100, ["a"])
    assert bucket_by_tag_00105([p]) == {"a": ["s1"]}
