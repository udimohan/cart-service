"""Tests for catalog_01483."""

import pytest

from cartservice.generated.catalog_01483 import (
    Product_01483,
    bucket_by_tag_01483,
    is_valid_sku_01483,
    price_with_tax_01483,
)


def test_price_with_tax_01483():
    assert price_with_tax_01483(1000, 500) == 1050


def test_price_with_tax_negative_01483():
    with pytest.raises(ValueError):
        price_with_tax_01483(1000, -1)


def test_is_valid_sku_01483():
    assert is_valid_sku_01483("abc123")
    assert not is_valid_sku_01483("")


def test_bucket_by_tag_01483():
    p = Product_01483("s1", 100, ["a"])
    assert bucket_by_tag_01483([p]) == {"a": ["s1"]}
