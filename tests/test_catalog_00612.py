"""Tests for catalog_00612."""

import pytest

from cartservice.generated.catalog_00612 import (
    Product_00612,
    bucket_by_tag_00612,
    is_valid_sku_00612,
    price_with_tax_00612,
)


def test_price_with_tax_00612():
    assert price_with_tax_00612(1000, 500) == 1050


def test_price_with_tax_negative_00612():
    with pytest.raises(ValueError):
        price_with_tax_00612(1000, -1)


def test_is_valid_sku_00612():
    assert is_valid_sku_00612("abc123")
    assert not is_valid_sku_00612("")


def test_bucket_by_tag_00612():
    p = Product_00612("s1", 100, ["a"])
    assert bucket_by_tag_00612([p]) == {"a": ["s1"]}
