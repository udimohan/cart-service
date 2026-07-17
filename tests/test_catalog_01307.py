"""Tests for catalog_01307."""

import pytest

from cartservice.generated.catalog_01307 import (
    Product_01307,
    bucket_by_tag_01307,
    is_valid_sku_01307,
    price_with_tax_01307,
)


def test_price_with_tax_01307():
    assert price_with_tax_01307(1000, 500) == 1050


def test_price_with_tax_negative_01307():
    with pytest.raises(ValueError):
        price_with_tax_01307(1000, -1)


def test_is_valid_sku_01307():
    assert is_valid_sku_01307("abc123")
    assert not is_valid_sku_01307("")


def test_bucket_by_tag_01307():
    p = Product_01307("s1", 100, ["a"])
    assert bucket_by_tag_01307([p]) == {"a": ["s1"]}
