"""Tests for catalog_00602."""

import pytest

from cartservice.generated.catalog_00602 import (
    Product_00602,
    bucket_by_tag_00602,
    is_valid_sku_00602,
    price_with_tax_00602,
)


def test_price_with_tax_00602():
    assert price_with_tax_00602(1000, 500) == 1050


def test_price_with_tax_negative_00602():
    with pytest.raises(ValueError):
        price_with_tax_00602(1000, -1)


def test_is_valid_sku_00602():
    assert is_valid_sku_00602("abc123")
    assert not is_valid_sku_00602("")


def test_bucket_by_tag_00602():
    p = Product_00602("s1", 100, ["a"])
    assert bucket_by_tag_00602([p]) == {"a": ["s1"]}
