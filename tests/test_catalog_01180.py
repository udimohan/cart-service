"""Tests for catalog_01180."""

import pytest

from cartservice.generated.catalog_01180 import (
    Product_01180,
    bucket_by_tag_01180,
    is_valid_sku_01180,
    price_with_tax_01180,
)


def test_price_with_tax_01180():
    assert price_with_tax_01180(1000, 500) == 1050


def test_price_with_tax_negative_01180():
    with pytest.raises(ValueError):
        price_with_tax_01180(1000, -1)


def test_is_valid_sku_01180():
    assert is_valid_sku_01180("abc123")
    assert not is_valid_sku_01180("")


def test_bucket_by_tag_01180():
    p = Product_01180("s1", 100, ["a"])
    assert bucket_by_tag_01180([p]) == {"a": ["s1"]}
