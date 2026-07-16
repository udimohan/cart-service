"""Tests for catalog_01035."""

import pytest

from cartservice.generated.catalog_01035 import (
    Product_01035,
    bucket_by_tag_01035,
    is_valid_sku_01035,
    price_with_tax_01035,
)


def test_price_with_tax_01035():
    assert price_with_tax_01035(1000, 500) == 1050


def test_price_with_tax_negative_01035():
    with pytest.raises(ValueError):
        price_with_tax_01035(1000, -1)


def test_is_valid_sku_01035():
    assert is_valid_sku_01035("abc123")
    assert not is_valid_sku_01035("")


def test_bucket_by_tag_01035():
    p = Product_01035("s1", 100, ["a"])
    assert bucket_by_tag_01035([p]) == {"a": ["s1"]}
