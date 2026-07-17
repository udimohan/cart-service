"""Tests for catalog_01123."""

import pytest

from cartservice.generated.catalog_01123 import (
    Product_01123,
    bucket_by_tag_01123,
    is_valid_sku_01123,
    price_with_tax_01123,
)


def test_price_with_tax_01123():
    assert price_with_tax_01123(1000, 500) == 1050


def test_price_with_tax_negative_01123():
    with pytest.raises(ValueError):
        price_with_tax_01123(1000, -1)


def test_is_valid_sku_01123():
    assert is_valid_sku_01123("abc123")
    assert not is_valid_sku_01123("")


def test_bucket_by_tag_01123():
    p = Product_01123("s1", 100, ["a"])
    assert bucket_by_tag_01123([p]) == {"a": ["s1"]}
