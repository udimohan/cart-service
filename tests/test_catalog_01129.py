"""Tests for catalog_01129."""

import pytest

from cartservice.generated.catalog_01129 import (
    Product_01129,
    bucket_by_tag_01129,
    is_valid_sku_01129,
    price_with_tax_01129,
)


def test_price_with_tax_01129():
    assert price_with_tax_01129(1000, 500) == 1050


def test_price_with_tax_negative_01129():
    with pytest.raises(ValueError):
        price_with_tax_01129(1000, -1)


def test_is_valid_sku_01129():
    assert is_valid_sku_01129("abc123")
    assert not is_valid_sku_01129("")


def test_bucket_by_tag_01129():
    p = Product_01129("s1", 100, ["a"])
    assert bucket_by_tag_01129([p]) == {"a": ["s1"]}
