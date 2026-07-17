"""Tests for catalog_00011."""

import pytest

from cartservice.generated.catalog_00011 import (
    Product_00011,
    bucket_by_tag_00011,
    is_valid_sku_00011,
    price_with_tax_00011,
)


def test_price_with_tax_00011():
    assert price_with_tax_00011(1000, 500) == 1050


def test_price_with_tax_negative_00011():
    with pytest.raises(ValueError):
        price_with_tax_00011(1000, -1)


def test_is_valid_sku_00011():
    assert is_valid_sku_00011("abc123")
    assert not is_valid_sku_00011("")


def test_bucket_by_tag_00011():
    p = Product_00011("s1", 100, ["a"])
    assert bucket_by_tag_00011([p]) == {"a": ["s1"]}
