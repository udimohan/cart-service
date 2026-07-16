"""Tests for catalog_00213."""

import pytest

from cartservice.generated.catalog_00213 import (
    Product_00213,
    bucket_by_tag_00213,
    is_valid_sku_00213,
    price_with_tax_00213,
)


def test_price_with_tax_00213():
    assert price_with_tax_00213(1000, 500) == 1050


def test_price_with_tax_negative_00213():
    with pytest.raises(ValueError):
        price_with_tax_00213(1000, -1)


def test_is_valid_sku_00213():
    assert is_valid_sku_00213("abc123")
    assert not is_valid_sku_00213("")


def test_bucket_by_tag_00213():
    p = Product_00213("s1", 100, ["a"])
    assert bucket_by_tag_00213([p]) == {"a": ["s1"]}
