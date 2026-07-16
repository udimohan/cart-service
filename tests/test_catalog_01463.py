"""Tests for catalog_01463."""

import pytest

from cartservice.generated.catalog_01463 import (
    Product_01463,
    bucket_by_tag_01463,
    is_valid_sku_01463,
    price_with_tax_01463,
)


def test_price_with_tax_01463():
    assert price_with_tax_01463(1000, 500) == 1050


def test_price_with_tax_negative_01463():
    with pytest.raises(ValueError):
        price_with_tax_01463(1000, -1)


def test_is_valid_sku_01463():
    assert is_valid_sku_01463("abc123")
    assert not is_valid_sku_01463("")


def test_bucket_by_tag_01463():
    p = Product_01463("s1", 100, ["a"])
    assert bucket_by_tag_01463([p]) == {"a": ["s1"]}
