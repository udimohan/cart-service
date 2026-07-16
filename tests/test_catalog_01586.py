"""Tests for catalog_01586."""

import pytest

from cartservice.generated.catalog_01586 import (
    Product_01586,
    bucket_by_tag_01586,
    is_valid_sku_01586,
    price_with_tax_01586,
)


def test_price_with_tax_01586():
    assert price_with_tax_01586(1000, 500) == 1050


def test_price_with_tax_negative_01586():
    with pytest.raises(ValueError):
        price_with_tax_01586(1000, -1)


def test_is_valid_sku_01586():
    assert is_valid_sku_01586("abc123")
    assert not is_valid_sku_01586("")


def test_bucket_by_tag_01586():
    p = Product_01586("s1", 100, ["a"])
    assert bucket_by_tag_01586([p]) == {"a": ["s1"]}
