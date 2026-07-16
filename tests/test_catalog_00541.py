"""Tests for catalog_00541."""

import pytest

from cartservice.generated.catalog_00541 import (
    Product_00541,
    bucket_by_tag_00541,
    is_valid_sku_00541,
    price_with_tax_00541,
)


def test_price_with_tax_00541():
    assert price_with_tax_00541(1000, 500) == 1050


def test_price_with_tax_negative_00541():
    with pytest.raises(ValueError):
        price_with_tax_00541(1000, -1)


def test_is_valid_sku_00541():
    assert is_valid_sku_00541("abc123")
    assert not is_valid_sku_00541("")


def test_bucket_by_tag_00541():
    p = Product_00541("s1", 100, ["a"])
    assert bucket_by_tag_00541([p]) == {"a": ["s1"]}
