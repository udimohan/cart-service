"""Tests for catalog_01412."""

import pytest

from cartservice.generated.catalog_01412 import (
    Product_01412,
    bucket_by_tag_01412,
    is_valid_sku_01412,
    price_with_tax_01412,
)


def test_price_with_tax_01412():
    assert price_with_tax_01412(1000, 500) == 1050


def test_price_with_tax_negative_01412():
    with pytest.raises(ValueError):
        price_with_tax_01412(1000, -1)


def test_is_valid_sku_01412():
    assert is_valid_sku_01412("abc123")
    assert not is_valid_sku_01412("")


def test_bucket_by_tag_01412():
    p = Product_01412("s1", 100, ["a"])
    assert bucket_by_tag_01412([p]) == {"a": ["s1"]}
