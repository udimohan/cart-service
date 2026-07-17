"""Tests for catalog_01000."""

import pytest

from cartservice.generated.catalog_01000 import (
    Product_01000,
    bucket_by_tag_01000,
    is_valid_sku_01000,
    price_with_tax_01000,
)


def test_price_with_tax_01000():
    assert price_with_tax_01000(1000, 500) == 1050


def test_price_with_tax_negative_01000():
    with pytest.raises(ValueError):
        price_with_tax_01000(1000, -1)


def test_is_valid_sku_01000():
    assert is_valid_sku_01000("abc123")
    assert not is_valid_sku_01000("")


def test_bucket_by_tag_01000():
    p = Product_01000("s1", 100, ["a"])
    assert bucket_by_tag_01000([p]) == {"a": ["s1"]}
