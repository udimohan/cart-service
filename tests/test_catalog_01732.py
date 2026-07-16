"""Tests for catalog_01732."""

import pytest

from cartservice.generated.catalog_01732 import (
    Product_01732,
    bucket_by_tag_01732,
    is_valid_sku_01732,
    price_with_tax_01732,
)


def test_price_with_tax_01732():
    assert price_with_tax_01732(1000, 500) == 1050


def test_price_with_tax_negative_01732():
    with pytest.raises(ValueError):
        price_with_tax_01732(1000, -1)


def test_is_valid_sku_01732():
    assert is_valid_sku_01732("abc123")
    assert not is_valid_sku_01732("")


def test_bucket_by_tag_01732():
    p = Product_01732("s1", 100, ["a"])
    assert bucket_by_tag_01732([p]) == {"a": ["s1"]}
