"""Tests for catalog_01387."""

import pytest

from cartservice.generated.catalog_01387 import (
    Product_01387,
    bucket_by_tag_01387,
    is_valid_sku_01387,
    price_with_tax_01387,
)


def test_price_with_tax_01387():
    assert price_with_tax_01387(1000, 500) == 1050


def test_price_with_tax_negative_01387():
    with pytest.raises(ValueError):
        price_with_tax_01387(1000, -1)


def test_is_valid_sku_01387():
    assert is_valid_sku_01387("abc123")
    assert not is_valid_sku_01387("")


def test_bucket_by_tag_01387():
    p = Product_01387("s1", 100, ["a"])
    assert bucket_by_tag_01387([p]) == {"a": ["s1"]}
