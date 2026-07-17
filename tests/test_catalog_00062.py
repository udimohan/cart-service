"""Tests for catalog_00062."""

import pytest

from cartservice.generated.catalog_00062 import (
    Product_00062,
    bucket_by_tag_00062,
    is_valid_sku_00062,
    price_with_tax_00062,
)


def test_price_with_tax_00062():
    assert price_with_tax_00062(1000, 500) == 1050


def test_price_with_tax_negative_00062():
    with pytest.raises(ValueError):
        price_with_tax_00062(1000, -1)


def test_is_valid_sku_00062():
    assert is_valid_sku_00062("abc123")
    assert not is_valid_sku_00062("")


def test_bucket_by_tag_00062():
    p = Product_00062("s1", 100, ["a"])
    assert bucket_by_tag_00062([p]) == {"a": ["s1"]}
