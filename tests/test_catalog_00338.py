"""Tests for catalog_00338."""

import pytest

from cartservice.generated.catalog_00338 import (
    Product_00338,
    bucket_by_tag_00338,
    is_valid_sku_00338,
    price_with_tax_00338,
)


def test_price_with_tax_00338():
    assert price_with_tax_00338(1000, 500) == 1050


def test_price_with_tax_negative_00338():
    with pytest.raises(ValueError):
        price_with_tax_00338(1000, -1)


def test_is_valid_sku_00338():
    assert is_valid_sku_00338("abc123")
    assert not is_valid_sku_00338("")


def test_bucket_by_tag_00338():
    p = Product_00338("s1", 100, ["a"])
    assert bucket_by_tag_00338([p]) == {"a": ["s1"]}
