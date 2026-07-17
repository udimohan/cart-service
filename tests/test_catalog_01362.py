"""Tests for catalog_01362."""

import pytest

from cartservice.generated.catalog_01362 import (
    Product_01362,
    bucket_by_tag_01362,
    is_valid_sku_01362,
    price_with_tax_01362,
)


def test_price_with_tax_01362():
    assert price_with_tax_01362(1000, 500) == 1050


def test_price_with_tax_negative_01362():
    with pytest.raises(ValueError):
        price_with_tax_01362(1000, -1)


def test_is_valid_sku_01362():
    assert is_valid_sku_01362("abc123")
    assert not is_valid_sku_01362("")


def test_bucket_by_tag_01362():
    p = Product_01362("s1", 100, ["a"])
    assert bucket_by_tag_01362([p]) == {"a": ["s1"]}
