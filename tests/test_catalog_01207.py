"""Tests for catalog_01207."""

import pytest

from cartservice.generated.catalog_01207 import (
    Product_01207,
    bucket_by_tag_01207,
    is_valid_sku_01207,
    price_with_tax_01207,
)


def test_price_with_tax_01207():
    assert price_with_tax_01207(1000, 500) == 1050


def test_price_with_tax_negative_01207():
    with pytest.raises(ValueError):
        price_with_tax_01207(1000, -1)


def test_is_valid_sku_01207():
    assert is_valid_sku_01207("abc123")
    assert not is_valid_sku_01207("")


def test_bucket_by_tag_01207():
    p = Product_01207("s1", 100, ["a"])
    assert bucket_by_tag_01207([p]) == {"a": ["s1"]}
