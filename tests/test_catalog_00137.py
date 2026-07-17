"""Tests for catalog_00137."""

import pytest

from cartservice.generated.catalog_00137 import (
    Product_00137,
    bucket_by_tag_00137,
    is_valid_sku_00137,
    price_with_tax_00137,
)


def test_price_with_tax_00137():
    assert price_with_tax_00137(1000, 500) == 1050


def test_price_with_tax_negative_00137():
    with pytest.raises(ValueError):
        price_with_tax_00137(1000, -1)


def test_is_valid_sku_00137():
    assert is_valid_sku_00137("abc123")
    assert not is_valid_sku_00137("")


def test_bucket_by_tag_00137():
    p = Product_00137("s1", 100, ["a"])
    assert bucket_by_tag_00137([p]) == {"a": ["s1"]}
