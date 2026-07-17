"""Tests for catalog_00971."""

import pytest

from cartservice.generated.catalog_00971 import (
    Product_00971,
    bucket_by_tag_00971,
    is_valid_sku_00971,
    price_with_tax_00971,
)


def test_price_with_tax_00971():
    assert price_with_tax_00971(1000, 500) == 1050


def test_price_with_tax_negative_00971():
    with pytest.raises(ValueError):
        price_with_tax_00971(1000, -1)


def test_is_valid_sku_00971():
    assert is_valid_sku_00971("abc123")
    assert not is_valid_sku_00971("")


def test_bucket_by_tag_00971():
    p = Product_00971("s1", 100, ["a"])
    assert bucket_by_tag_00971([p]) == {"a": ["s1"]}
