"""Tests for catalog_00345."""

import pytest

from cartservice.generated.catalog_00345 import (
    Product_00345,
    bucket_by_tag_00345,
    is_valid_sku_00345,
    price_with_tax_00345,
)


def test_price_with_tax_00345():
    assert price_with_tax_00345(1000, 500) == 1050


def test_price_with_tax_negative_00345():
    with pytest.raises(ValueError):
        price_with_tax_00345(1000, -1)


def test_is_valid_sku_00345():
    assert is_valid_sku_00345("abc123")
    assert not is_valid_sku_00345("")


def test_bucket_by_tag_00345():
    p = Product_00345("s1", 100, ["a"])
    assert bucket_by_tag_00345([p]) == {"a": ["s1"]}
