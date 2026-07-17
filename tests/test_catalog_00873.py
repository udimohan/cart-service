"""Tests for catalog_00873."""

import pytest

from cartservice.generated.catalog_00873 import (
    Product_00873,
    bucket_by_tag_00873,
    is_valid_sku_00873,
    price_with_tax_00873,
)


def test_price_with_tax_00873():
    assert price_with_tax_00873(1000, 500) == 1050


def test_price_with_tax_negative_00873():
    with pytest.raises(ValueError):
        price_with_tax_00873(1000, -1)


def test_is_valid_sku_00873():
    assert is_valid_sku_00873("abc123")
    assert not is_valid_sku_00873("")


def test_bucket_by_tag_00873():
    p = Product_00873("s1", 100, ["a"])
    assert bucket_by_tag_00873([p]) == {"a": ["s1"]}
