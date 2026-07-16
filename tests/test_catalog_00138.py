"""Tests for catalog_00138."""

import pytest

from cartservice.generated.catalog_00138 import (
    Product_00138,
    bucket_by_tag_00138,
    is_valid_sku_00138,
    price_with_tax_00138,
)


def test_price_with_tax_00138():
    assert price_with_tax_00138(1000, 500) == 1050


def test_price_with_tax_negative_00138():
    with pytest.raises(ValueError):
        price_with_tax_00138(1000, -1)


def test_is_valid_sku_00138():
    assert is_valid_sku_00138("abc123")
    assert not is_valid_sku_00138("")


def test_bucket_by_tag_00138():
    p = Product_00138("s1", 100, ["a"])
    assert bucket_by_tag_00138([p]) == {"a": ["s1"]}
