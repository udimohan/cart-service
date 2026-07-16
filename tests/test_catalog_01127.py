"""Tests for catalog_01127."""

import pytest

from cartservice.generated.catalog_01127 import (
    Product_01127,
    bucket_by_tag_01127,
    is_valid_sku_01127,
    price_with_tax_01127,
)


def test_price_with_tax_01127():
    assert price_with_tax_01127(1000, 500) == 1050


def test_price_with_tax_negative_01127():
    with pytest.raises(ValueError):
        price_with_tax_01127(1000, -1)


def test_is_valid_sku_01127():
    assert is_valid_sku_01127("abc123")
    assert not is_valid_sku_01127("")


def test_bucket_by_tag_01127():
    p = Product_01127("s1", 100, ["a"])
    assert bucket_by_tag_01127([p]) == {"a": ["s1"]}
