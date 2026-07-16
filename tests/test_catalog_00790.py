"""Tests for catalog_00790."""

import pytest

from cartservice.generated.catalog_00790 import (
    Product_00790,
    bucket_by_tag_00790,
    is_valid_sku_00790,
    price_with_tax_00790,
)


def test_price_with_tax_00790():
    assert price_with_tax_00790(1000, 500) == 1050


def test_price_with_tax_negative_00790():
    with pytest.raises(ValueError):
        price_with_tax_00790(1000, -1)


def test_is_valid_sku_00790():
    assert is_valid_sku_00790("abc123")
    assert not is_valid_sku_00790("")


def test_bucket_by_tag_00790():
    p = Product_00790("s1", 100, ["a"])
    assert bucket_by_tag_00790([p]) == {"a": ["s1"]}
