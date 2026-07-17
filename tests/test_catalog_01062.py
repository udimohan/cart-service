"""Tests for catalog_01062."""

import pytest

from cartservice.generated.catalog_01062 import (
    Product_01062,
    bucket_by_tag_01062,
    is_valid_sku_01062,
    price_with_tax_01062,
)


def test_price_with_tax_01062():
    assert price_with_tax_01062(1000, 500) == 1050


def test_price_with_tax_negative_01062():
    with pytest.raises(ValueError):
        price_with_tax_01062(1000, -1)


def test_is_valid_sku_01062():
    assert is_valid_sku_01062("abc123")
    assert not is_valid_sku_01062("")


def test_bucket_by_tag_01062():
    p = Product_01062("s1", 100, ["a"])
    assert bucket_by_tag_01062([p]) == {"a": ["s1"]}
