"""Tests for catalog_00401."""

import pytest

from cartservice.generated.catalog_00401 import (
    Product_00401,
    bucket_by_tag_00401,
    is_valid_sku_00401,
    price_with_tax_00401,
)


def test_price_with_tax_00401():
    assert price_with_tax_00401(1000, 500) == 1050


def test_price_with_tax_negative_00401():
    with pytest.raises(ValueError):
        price_with_tax_00401(1000, -1)


def test_is_valid_sku_00401():
    assert is_valid_sku_00401("abc123")
    assert not is_valid_sku_00401("")


def test_bucket_by_tag_00401():
    p = Product_00401("s1", 100, ["a"])
    assert bucket_by_tag_00401([p]) == {"a": ["s1"]}
