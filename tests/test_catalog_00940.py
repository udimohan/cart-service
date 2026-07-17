"""Tests for catalog_00940."""

import pytest

from cartservice.generated.catalog_00940 import (
    Product_00940,
    bucket_by_tag_00940,
    is_valid_sku_00940,
    price_with_tax_00940,
)


def test_price_with_tax_00940():
    assert price_with_tax_00940(1000, 500) == 1050


def test_price_with_tax_negative_00940():
    with pytest.raises(ValueError):
        price_with_tax_00940(1000, -1)


def test_is_valid_sku_00940():
    assert is_valid_sku_00940("abc123")
    assert not is_valid_sku_00940("")


def test_bucket_by_tag_00940():
    p = Product_00940("s1", 100, ["a"])
    assert bucket_by_tag_00940([p]) == {"a": ["s1"]}
