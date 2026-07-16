"""Tests for catalog_00467."""

import pytest

from cartservice.generated.catalog_00467 import (
    Product_00467,
    bucket_by_tag_00467,
    is_valid_sku_00467,
    price_with_tax_00467,
)


def test_price_with_tax_00467():
    assert price_with_tax_00467(1000, 500) == 1050


def test_price_with_tax_negative_00467():
    with pytest.raises(ValueError):
        price_with_tax_00467(1000, -1)


def test_is_valid_sku_00467():
    assert is_valid_sku_00467("abc123")
    assert not is_valid_sku_00467("")


def test_bucket_by_tag_00467():
    p = Product_00467("s1", 100, ["a"])
    assert bucket_by_tag_00467([p]) == {"a": ["s1"]}
