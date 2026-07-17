"""Tests for catalog_00218."""

import pytest

from cartservice.generated.catalog_00218 import (
    Product_00218,
    bucket_by_tag_00218,
    is_valid_sku_00218,
    price_with_tax_00218,
)


def test_price_with_tax_00218():
    assert price_with_tax_00218(1000, 500) == 1050


def test_price_with_tax_negative_00218():
    with pytest.raises(ValueError):
        price_with_tax_00218(1000, -1)


def test_is_valid_sku_00218():
    assert is_valid_sku_00218("abc123")
    assert not is_valid_sku_00218("")


def test_bucket_by_tag_00218():
    p = Product_00218("s1", 100, ["a"])
    assert bucket_by_tag_00218([p]) == {"a": ["s1"]}
