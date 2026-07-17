"""Tests for catalog_00732."""

import pytest

from cartservice.generated.catalog_00732 import (
    Product_00732,
    bucket_by_tag_00732,
    is_valid_sku_00732,
    price_with_tax_00732,
)


def test_price_with_tax_00732():
    assert price_with_tax_00732(1000, 500) == 1050


def test_price_with_tax_negative_00732():
    with pytest.raises(ValueError):
        price_with_tax_00732(1000, -1)


def test_is_valid_sku_00732():
    assert is_valid_sku_00732("abc123")
    assert not is_valid_sku_00732("")


def test_bucket_by_tag_00732():
    p = Product_00732("s1", 100, ["a"])
    assert bucket_by_tag_00732([p]) == {"a": ["s1"]}
