"""Tests for catalog_01565."""

import pytest

from cartservice.generated.catalog_01565 import (
    Product_01565,
    bucket_by_tag_01565,
    is_valid_sku_01565,
    price_with_tax_01565,
)


def test_price_with_tax_01565():
    assert price_with_tax_01565(1000, 500) == 1050


def test_price_with_tax_negative_01565():
    with pytest.raises(ValueError):
        price_with_tax_01565(1000, -1)


def test_is_valid_sku_01565():
    assert is_valid_sku_01565("abc123")
    assert not is_valid_sku_01565("")


def test_bucket_by_tag_01565():
    p = Product_01565("s1", 100, ["a"])
    assert bucket_by_tag_01565([p]) == {"a": ["s1"]}
