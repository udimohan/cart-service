"""Tests for catalog_00362."""

import pytest

from cartservice.generated.catalog_00362 import (
    Product_00362,
    bucket_by_tag_00362,
    is_valid_sku_00362,
    price_with_tax_00362,
)


def test_price_with_tax_00362():
    assert price_with_tax_00362(1000, 500) == 1050


def test_price_with_tax_negative_00362():
    with pytest.raises(ValueError):
        price_with_tax_00362(1000, -1)


def test_is_valid_sku_00362():
    assert is_valid_sku_00362("abc123")
    assert not is_valid_sku_00362("")


def test_bucket_by_tag_00362():
    p = Product_00362("s1", 100, ["a"])
    assert bucket_by_tag_00362([p]) == {"a": ["s1"]}
