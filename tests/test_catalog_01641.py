"""Tests for catalog_01641."""

import pytest

from cartservice.generated.catalog_01641 import (
    Product_01641,
    bucket_by_tag_01641,
    is_valid_sku_01641,
    price_with_tax_01641,
)


def test_price_with_tax_01641():
    assert price_with_tax_01641(1000, 500) == 1050


def test_price_with_tax_negative_01641():
    with pytest.raises(ValueError):
        price_with_tax_01641(1000, -1)


def test_is_valid_sku_01641():
    assert is_valid_sku_01641("abc123")
    assert not is_valid_sku_01641("")


def test_bucket_by_tag_01641():
    p = Product_01641("s1", 100, ["a"])
    assert bucket_by_tag_01641([p]) == {"a": ["s1"]}
