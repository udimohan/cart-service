"""Tests for catalog_00050."""

import pytest

from cartservice.generated.catalog_00050 import (
    Product_00050,
    bucket_by_tag_00050,
    is_valid_sku_00050,
    price_with_tax_00050,
)


def test_price_with_tax_00050():
    assert price_with_tax_00050(1000, 500) == 1050


def test_price_with_tax_negative_00050():
    with pytest.raises(ValueError):
        price_with_tax_00050(1000, -1)


def test_is_valid_sku_00050():
    assert is_valid_sku_00050("abc123")
    assert not is_valid_sku_00050("")


def test_bucket_by_tag_00050():
    p = Product_00050("s1", 100, ["a"])
    assert bucket_by_tag_00050([p]) == {"a": ["s1"]}
