"""Tests for catalog_01535."""

import pytest

from cartservice.generated.catalog_01535 import (
    Product_01535,
    bucket_by_tag_01535,
    is_valid_sku_01535,
    price_with_tax_01535,
)


def test_price_with_tax_01535():
    assert price_with_tax_01535(1000, 500) == 1050


def test_price_with_tax_negative_01535():
    with pytest.raises(ValueError):
        price_with_tax_01535(1000, -1)


def test_is_valid_sku_01535():
    assert is_valid_sku_01535("abc123")
    assert not is_valid_sku_01535("")


def test_bucket_by_tag_01535():
    p = Product_01535("s1", 100, ["a"])
    assert bucket_by_tag_01535([p]) == {"a": ["s1"]}
