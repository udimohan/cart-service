"""Tests for catalog_00578."""

import pytest

from cartservice.generated.catalog_00578 import (
    Product_00578,
    bucket_by_tag_00578,
    is_valid_sku_00578,
    price_with_tax_00578,
)


def test_price_with_tax_00578():
    assert price_with_tax_00578(1000, 500) == 1050


def test_price_with_tax_negative_00578():
    with pytest.raises(ValueError):
        price_with_tax_00578(1000, -1)


def test_is_valid_sku_00578():
    assert is_valid_sku_00578("abc123")
    assert not is_valid_sku_00578("")


def test_bucket_by_tag_00578():
    p = Product_00578("s1", 100, ["a"])
    assert bucket_by_tag_00578([p]) == {"a": ["s1"]}
