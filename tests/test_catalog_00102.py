"""Tests for catalog_00102."""

import pytest

from cartservice.generated.catalog_00102 import (
    Product_00102,
    bucket_by_tag_00102,
    is_valid_sku_00102,
    price_with_tax_00102,
)


def test_price_with_tax_00102():
    assert price_with_tax_00102(1000, 500) == 1050


def test_price_with_tax_negative_00102():
    with pytest.raises(ValueError):
        price_with_tax_00102(1000, -1)


def test_is_valid_sku_00102():
    assert is_valid_sku_00102("abc123")
    assert not is_valid_sku_00102("")


def test_bucket_by_tag_00102():
    p = Product_00102("s1", 100, ["a"])
    assert bucket_by_tag_00102([p]) == {"a": ["s1"]}
