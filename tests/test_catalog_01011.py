"""Tests for catalog_01011."""

import pytest

from cartservice.generated.catalog_01011 import (
    Product_01011,
    bucket_by_tag_01011,
    is_valid_sku_01011,
    price_with_tax_01011,
)


def test_price_with_tax_01011():
    assert price_with_tax_01011(1000, 500) == 1050


def test_price_with_tax_negative_01011():
    with pytest.raises(ValueError):
        price_with_tax_01011(1000, -1)


def test_is_valid_sku_01011():
    assert is_valid_sku_01011("abc123")
    assert not is_valid_sku_01011("")


def test_bucket_by_tag_01011():
    p = Product_01011("s1", 100, ["a"])
    assert bucket_by_tag_01011([p]) == {"a": ["s1"]}
