"""Tests for catalog_00983."""

import pytest

from cartservice.generated.catalog_00983 import (
    Product_00983,
    bucket_by_tag_00983,
    is_valid_sku_00983,
    price_with_tax_00983,
)


def test_price_with_tax_00983():
    assert price_with_tax_00983(1000, 500) == 1050


def test_price_with_tax_negative_00983():
    with pytest.raises(ValueError):
        price_with_tax_00983(1000, -1)


def test_is_valid_sku_00983():
    assert is_valid_sku_00983("abc123")
    assert not is_valid_sku_00983("")


def test_bucket_by_tag_00983():
    p = Product_00983("s1", 100, ["a"])
    assert bucket_by_tag_00983([p]) == {"a": ["s1"]}
