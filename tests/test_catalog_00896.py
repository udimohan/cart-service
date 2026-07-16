"""Tests for catalog_00896."""

import pytest

from cartservice.generated.catalog_00896 import (
    Product_00896,
    bucket_by_tag_00896,
    is_valid_sku_00896,
    price_with_tax_00896,
)


def test_price_with_tax_00896():
    assert price_with_tax_00896(1000, 500) == 1050


def test_price_with_tax_negative_00896():
    with pytest.raises(ValueError):
        price_with_tax_00896(1000, -1)


def test_is_valid_sku_00896():
    assert is_valid_sku_00896("abc123")
    assert not is_valid_sku_00896("")


def test_bucket_by_tag_00896():
    p = Product_00896("s1", 100, ["a"])
    assert bucket_by_tag_00896([p]) == {"a": ["s1"]}
