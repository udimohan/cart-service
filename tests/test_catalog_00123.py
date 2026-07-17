"""Tests for catalog_00123."""

import pytest

from cartservice.generated.catalog_00123 import (
    Product_00123,
    bucket_by_tag_00123,
    is_valid_sku_00123,
    price_with_tax_00123,
)


def test_price_with_tax_00123():
    assert price_with_tax_00123(1000, 500) == 1050


def test_price_with_tax_negative_00123():
    with pytest.raises(ValueError):
        price_with_tax_00123(1000, -1)


def test_is_valid_sku_00123():
    assert is_valid_sku_00123("abc123")
    assert not is_valid_sku_00123("")


def test_bucket_by_tag_00123():
    p = Product_00123("s1", 100, ["a"])
    assert bucket_by_tag_00123([p]) == {"a": ["s1"]}
