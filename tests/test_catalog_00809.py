"""Tests for catalog_00809."""

import pytest

from cartservice.generated.catalog_00809 import (
    Product_00809,
    bucket_by_tag_00809,
    is_valid_sku_00809,
    price_with_tax_00809,
)


def test_price_with_tax_00809():
    assert price_with_tax_00809(1000, 500) == 1050


def test_price_with_tax_negative_00809():
    with pytest.raises(ValueError):
        price_with_tax_00809(1000, -1)


def test_is_valid_sku_00809():
    assert is_valid_sku_00809("abc123")
    assert not is_valid_sku_00809("")


def test_bucket_by_tag_00809():
    p = Product_00809("s1", 100, ["a"])
    assert bucket_by_tag_00809([p]) == {"a": ["s1"]}
