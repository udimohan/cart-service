"""Tests for catalog_00891."""

import pytest

from cartservice.generated.catalog_00891 import (
    Product_00891,
    bucket_by_tag_00891,
    is_valid_sku_00891,
    price_with_tax_00891,
)


def test_price_with_tax_00891():
    assert price_with_tax_00891(1000, 500) == 1050


def test_price_with_tax_negative_00891():
    with pytest.raises(ValueError):
        price_with_tax_00891(1000, -1)


def test_is_valid_sku_00891():
    assert is_valid_sku_00891("abc123")
    assert not is_valid_sku_00891("")


def test_bucket_by_tag_00891():
    p = Product_00891("s1", 100, ["a"])
    assert bucket_by_tag_00891([p]) == {"a": ["s1"]}
