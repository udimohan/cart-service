"""Tests for catalog_01464."""

import pytest

from cartservice.generated.catalog_01464 import (
    Product_01464,
    bucket_by_tag_01464,
    is_valid_sku_01464,
    price_with_tax_01464,
)


def test_price_with_tax_01464():
    assert price_with_tax_01464(1000, 500) == 1050


def test_price_with_tax_negative_01464():
    with pytest.raises(ValueError):
        price_with_tax_01464(1000, -1)


def test_is_valid_sku_01464():
    assert is_valid_sku_01464("abc123")
    assert not is_valid_sku_01464("")


def test_bucket_by_tag_01464():
    p = Product_01464("s1", 100, ["a"])
    assert bucket_by_tag_01464([p]) == {"a": ["s1"]}
