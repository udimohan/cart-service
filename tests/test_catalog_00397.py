"""Tests for catalog_00397."""

import pytest

from cartservice.generated.catalog_00397 import (
    Product_00397,
    bucket_by_tag_00397,
    is_valid_sku_00397,
    price_with_tax_00397,
)


def test_price_with_tax_00397():
    assert price_with_tax_00397(1000, 500) == 1050


def test_price_with_tax_negative_00397():
    with pytest.raises(ValueError):
        price_with_tax_00397(1000, -1)


def test_is_valid_sku_00397():
    assert is_valid_sku_00397("abc123")
    assert not is_valid_sku_00397("")


def test_bucket_by_tag_00397():
    p = Product_00397("s1", 100, ["a"])
    assert bucket_by_tag_00397([p]) == {"a": ["s1"]}
