"""Tests for catalog_00330."""

import pytest

from cartservice.generated.catalog_00330 import (
    Product_00330,
    bucket_by_tag_00330,
    is_valid_sku_00330,
    price_with_tax_00330,
)


def test_price_with_tax_00330():
    assert price_with_tax_00330(1000, 500) == 1050


def test_price_with_tax_negative_00330():
    with pytest.raises(ValueError):
        price_with_tax_00330(1000, -1)


def test_is_valid_sku_00330():
    assert is_valid_sku_00330("abc123")
    assert not is_valid_sku_00330("")


def test_bucket_by_tag_00330():
    p = Product_00330("s1", 100, ["a"])
    assert bucket_by_tag_00330([p]) == {"a": ["s1"]}
