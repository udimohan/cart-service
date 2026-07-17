"""Tests for catalog_00974."""

import pytest

from cartservice.generated.catalog_00974 import (
    Product_00974,
    bucket_by_tag_00974,
    is_valid_sku_00974,
    price_with_tax_00974,
)


def test_price_with_tax_00974():
    assert price_with_tax_00974(1000, 500) == 1050


def test_price_with_tax_negative_00974():
    with pytest.raises(ValueError):
        price_with_tax_00974(1000, -1)


def test_is_valid_sku_00974():
    assert is_valid_sku_00974("abc123")
    assert not is_valid_sku_00974("")


def test_bucket_by_tag_00974():
    p = Product_00974("s1", 100, ["a"])
    assert bucket_by_tag_00974([p]) == {"a": ["s1"]}
