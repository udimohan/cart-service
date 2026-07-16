"""Tests for catalog_00287."""

import pytest

from cartservice.generated.catalog_00287 import (
    Product_00287,
    bucket_by_tag_00287,
    is_valid_sku_00287,
    price_with_tax_00287,
)


def test_price_with_tax_00287():
    assert price_with_tax_00287(1000, 500) == 1050


def test_price_with_tax_negative_00287():
    with pytest.raises(ValueError):
        price_with_tax_00287(1000, -1)


def test_is_valid_sku_00287():
    assert is_valid_sku_00287("abc123")
    assert not is_valid_sku_00287("")


def test_bucket_by_tag_00287():
    p = Product_00287("s1", 100, ["a"])
    assert bucket_by_tag_00287([p]) == {"a": ["s1"]}
