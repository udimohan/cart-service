"""Tests for catalog_00170."""

import pytest

from cartservice.generated.catalog_00170 import (
    Product_00170,
    bucket_by_tag_00170,
    is_valid_sku_00170,
    price_with_tax_00170,
)


def test_price_with_tax_00170():
    assert price_with_tax_00170(1000, 500) == 1050


def test_price_with_tax_negative_00170():
    with pytest.raises(ValueError):
        price_with_tax_00170(1000, -1)


def test_is_valid_sku_00170():
    assert is_valid_sku_00170("abc123")
    assert not is_valid_sku_00170("")


def test_bucket_by_tag_00170():
    p = Product_00170("s1", 100, ["a"])
    assert bucket_by_tag_00170([p]) == {"a": ["s1"]}
