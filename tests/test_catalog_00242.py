"""Tests for catalog_00242."""

import pytest

from cartservice.generated.catalog_00242 import (
    Product_00242,
    bucket_by_tag_00242,
    is_valid_sku_00242,
    price_with_tax_00242,
)


def test_price_with_tax_00242():
    assert price_with_tax_00242(1000, 500) == 1050


def test_price_with_tax_negative_00242():
    with pytest.raises(ValueError):
        price_with_tax_00242(1000, -1)


def test_is_valid_sku_00242():
    assert is_valid_sku_00242("abc123")
    assert not is_valid_sku_00242("")


def test_bucket_by_tag_00242():
    p = Product_00242("s1", 100, ["a"])
    assert bucket_by_tag_00242([p]) == {"a": ["s1"]}
