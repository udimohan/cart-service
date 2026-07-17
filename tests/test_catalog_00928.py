"""Tests for catalog_00928."""

import pytest

from cartservice.generated.catalog_00928 import (
    Product_00928,
    bucket_by_tag_00928,
    is_valid_sku_00928,
    price_with_tax_00928,
)


def test_price_with_tax_00928():
    assert price_with_tax_00928(1000, 500) == 1050


def test_price_with_tax_negative_00928():
    with pytest.raises(ValueError):
        price_with_tax_00928(1000, -1)


def test_is_valid_sku_00928():
    assert is_valid_sku_00928("abc123")
    assert not is_valid_sku_00928("")


def test_bucket_by_tag_00928():
    p = Product_00928("s1", 100, ["a"])
    assert bucket_by_tag_00928([p]) == {"a": ["s1"]}
