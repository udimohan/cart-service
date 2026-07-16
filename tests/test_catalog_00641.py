"""Tests for catalog_00641."""

import pytest

from cartservice.generated.catalog_00641 import (
    Product_00641,
    bucket_by_tag_00641,
    is_valid_sku_00641,
    price_with_tax_00641,
)


def test_price_with_tax_00641():
    assert price_with_tax_00641(1000, 500) == 1050


def test_price_with_tax_negative_00641():
    with pytest.raises(ValueError):
        price_with_tax_00641(1000, -1)


def test_is_valid_sku_00641():
    assert is_valid_sku_00641("abc123")
    assert not is_valid_sku_00641("")


def test_bucket_by_tag_00641():
    p = Product_00641("s1", 100, ["a"])
    assert bucket_by_tag_00641([p]) == {"a": ["s1"]}
