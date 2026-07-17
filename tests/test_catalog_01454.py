"""Tests for catalog_01454."""

import pytest

from cartservice.generated.catalog_01454 import (
    Product_01454,
    bucket_by_tag_01454,
    is_valid_sku_01454,
    price_with_tax_01454,
)


def test_price_with_tax_01454():
    assert price_with_tax_01454(1000, 500) == 1050


def test_price_with_tax_negative_01454():
    with pytest.raises(ValueError):
        price_with_tax_01454(1000, -1)


def test_is_valid_sku_01454():
    assert is_valid_sku_01454("abc123")
    assert not is_valid_sku_01454("")


def test_bucket_by_tag_01454():
    p = Product_01454("s1", 100, ["a"])
    assert bucket_by_tag_01454([p]) == {"a": ["s1"]}
