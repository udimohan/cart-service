"""Tests for catalog_00851."""

import pytest

from cartservice.generated.catalog_00851 import (
    Product_00851,
    bucket_by_tag_00851,
    is_valid_sku_00851,
    price_with_tax_00851,
)


def test_price_with_tax_00851():
    assert price_with_tax_00851(1000, 500) == 1050


def test_price_with_tax_negative_00851():
    with pytest.raises(ValueError):
        price_with_tax_00851(1000, -1)


def test_is_valid_sku_00851():
    assert is_valid_sku_00851("abc123")
    assert not is_valid_sku_00851("")


def test_bucket_by_tag_00851():
    p = Product_00851("s1", 100, ["a"])
    assert bucket_by_tag_00851([p]) == {"a": ["s1"]}
