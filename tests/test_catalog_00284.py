"""Tests for catalog_00284."""

import pytest

from cartservice.generated.catalog_00284 import (
    Product_00284,
    bucket_by_tag_00284,
    is_valid_sku_00284,
    price_with_tax_00284,
)


def test_price_with_tax_00284():
    assert price_with_tax_00284(1000, 500) == 1050


def test_price_with_tax_negative_00284():
    with pytest.raises(ValueError):
        price_with_tax_00284(1000, -1)


def test_is_valid_sku_00284():
    assert is_valid_sku_00284("abc123")
    assert not is_valid_sku_00284("")


def test_bucket_by_tag_00284():
    p = Product_00284("s1", 100, ["a"])
    assert bucket_by_tag_00284([p]) == {"a": ["s1"]}
