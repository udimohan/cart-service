"""Tests for catalog_01052."""

import pytest

from cartservice.generated.catalog_01052 import (
    Product_01052,
    bucket_by_tag_01052,
    is_valid_sku_01052,
    price_with_tax_01052,
)


def test_price_with_tax_01052():
    assert price_with_tax_01052(1000, 500) == 1050


def test_price_with_tax_negative_01052():
    with pytest.raises(ValueError):
        price_with_tax_01052(1000, -1)


def test_is_valid_sku_01052():
    assert is_valid_sku_01052("abc123")
    assert not is_valid_sku_01052("")


def test_bucket_by_tag_01052():
    p = Product_01052("s1", 100, ["a"])
    assert bucket_by_tag_01052([p]) == {"a": ["s1"]}
