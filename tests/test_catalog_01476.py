"""Tests for catalog_01476."""

import pytest

from cartservice.generated.catalog_01476 import (
    Product_01476,
    bucket_by_tag_01476,
    is_valid_sku_01476,
    price_with_tax_01476,
)


def test_price_with_tax_01476():
    assert price_with_tax_01476(1000, 500) == 1050


def test_price_with_tax_negative_01476():
    with pytest.raises(ValueError):
        price_with_tax_01476(1000, -1)


def test_is_valid_sku_01476():
    assert is_valid_sku_01476("abc123")
    assert not is_valid_sku_01476("")


def test_bucket_by_tag_01476():
    p = Product_01476("s1", 100, ["a"])
    assert bucket_by_tag_01476([p]) == {"a": ["s1"]}
