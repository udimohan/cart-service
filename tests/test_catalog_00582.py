"""Tests for catalog_00582."""

import pytest

from cartservice.generated.catalog_00582 import (
    Product_00582,
    bucket_by_tag_00582,
    is_valid_sku_00582,
    price_with_tax_00582,
)


def test_price_with_tax_00582():
    assert price_with_tax_00582(1000, 500) == 1050


def test_price_with_tax_negative_00582():
    with pytest.raises(ValueError):
        price_with_tax_00582(1000, -1)


def test_is_valid_sku_00582():
    assert is_valid_sku_00582("abc123")
    assert not is_valid_sku_00582("")


def test_bucket_by_tag_00582():
    p = Product_00582("s1", 100, ["a"])
    assert bucket_by_tag_00582([p]) == {"a": ["s1"]}
