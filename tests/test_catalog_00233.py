"""Tests for catalog_00233."""

import pytest

from cartservice.generated.catalog_00233 import (
    Product_00233,
    bucket_by_tag_00233,
    is_valid_sku_00233,
    price_with_tax_00233,
)


def test_price_with_tax_00233():
    assert price_with_tax_00233(1000, 500) == 1050


def test_price_with_tax_negative_00233():
    with pytest.raises(ValueError):
        price_with_tax_00233(1000, -1)


def test_is_valid_sku_00233():
    assert is_valid_sku_00233("abc123")
    assert not is_valid_sku_00233("")


def test_bucket_by_tag_00233():
    p = Product_00233("s1", 100, ["a"])
    assert bucket_by_tag_00233([p]) == {"a": ["s1"]}
