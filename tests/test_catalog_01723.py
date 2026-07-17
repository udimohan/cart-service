"""Tests for catalog_01723."""

import pytest

from cartservice.generated.catalog_01723 import (
    Product_01723,
    bucket_by_tag_01723,
    is_valid_sku_01723,
    price_with_tax_01723,
)


def test_price_with_tax_01723():
    assert price_with_tax_01723(1000, 500) == 1050


def test_price_with_tax_negative_01723():
    with pytest.raises(ValueError):
        price_with_tax_01723(1000, -1)


def test_is_valid_sku_01723():
    assert is_valid_sku_01723("abc123")
    assert not is_valid_sku_01723("")


def test_bucket_by_tag_01723():
    p = Product_01723("s1", 100, ["a"])
    assert bucket_by_tag_01723([p]) == {"a": ["s1"]}
