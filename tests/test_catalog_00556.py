"""Tests for catalog_00556."""

import pytest

from cartservice.generated.catalog_00556 import (
    Product_00556,
    bucket_by_tag_00556,
    is_valid_sku_00556,
    price_with_tax_00556,
)


def test_price_with_tax_00556():
    assert price_with_tax_00556(1000, 500) == 1050


def test_price_with_tax_negative_00556():
    with pytest.raises(ValueError):
        price_with_tax_00556(1000, -1)


def test_is_valid_sku_00556():
    assert is_valid_sku_00556("abc123")
    assert not is_valid_sku_00556("")


def test_bucket_by_tag_00556():
    p = Product_00556("s1", 100, ["a"])
    assert bucket_by_tag_00556([p]) == {"a": ["s1"]}
