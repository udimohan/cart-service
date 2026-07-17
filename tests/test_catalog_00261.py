"""Tests for catalog_00261."""

import pytest

from cartservice.generated.catalog_00261 import (
    Product_00261,
    bucket_by_tag_00261,
    is_valid_sku_00261,
    price_with_tax_00261,
)


def test_price_with_tax_00261():
    assert price_with_tax_00261(1000, 500) == 1050


def test_price_with_tax_negative_00261():
    with pytest.raises(ValueError):
        price_with_tax_00261(1000, -1)


def test_is_valid_sku_00261():
    assert is_valid_sku_00261("abc123")
    assert not is_valid_sku_00261("")


def test_bucket_by_tag_00261():
    p = Product_00261("s1", 100, ["a"])
    assert bucket_by_tag_00261([p]) == {"a": ["s1"]}
