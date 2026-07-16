"""Tests for catalog_00425."""

import pytest

from cartservice.generated.catalog_00425 import (
    Product_00425,
    bucket_by_tag_00425,
    is_valid_sku_00425,
    price_with_tax_00425,
)


def test_price_with_tax_00425():
    assert price_with_tax_00425(1000, 500) == 1050


def test_price_with_tax_negative_00425():
    with pytest.raises(ValueError):
        price_with_tax_00425(1000, -1)


def test_is_valid_sku_00425():
    assert is_valid_sku_00425("abc123")
    assert not is_valid_sku_00425("")


def test_bucket_by_tag_00425():
    p = Product_00425("s1", 100, ["a"])
    assert bucket_by_tag_00425([p]) == {"a": ["s1"]}
