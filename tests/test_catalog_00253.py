"""Tests for catalog_00253."""

import pytest

from cartservice.generated.catalog_00253 import (
    Product_00253,
    bucket_by_tag_00253,
    is_valid_sku_00253,
    price_with_tax_00253,
)


def test_price_with_tax_00253():
    assert price_with_tax_00253(1000, 500) == 1050


def test_price_with_tax_negative_00253():
    with pytest.raises(ValueError):
        price_with_tax_00253(1000, -1)


def test_is_valid_sku_00253():
    assert is_valid_sku_00253("abc123")
    assert not is_valid_sku_00253("")


def test_bucket_by_tag_00253():
    p = Product_00253("s1", 100, ["a"])
    assert bucket_by_tag_00253([p]) == {"a": ["s1"]}
