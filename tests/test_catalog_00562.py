"""Tests for catalog_00562."""

import pytest

from cartservice.generated.catalog_00562 import (
    Product_00562,
    bucket_by_tag_00562,
    is_valid_sku_00562,
    price_with_tax_00562,
)


def test_price_with_tax_00562():
    assert price_with_tax_00562(1000, 500) == 1050


def test_price_with_tax_negative_00562():
    with pytest.raises(ValueError):
        price_with_tax_00562(1000, -1)


def test_is_valid_sku_00562():
    assert is_valid_sku_00562("abc123")
    assert not is_valid_sku_00562("")


def test_bucket_by_tag_00562():
    p = Product_00562("s1", 100, ["a"])
    assert bucket_by_tag_00562([p]) == {"a": ["s1"]}
