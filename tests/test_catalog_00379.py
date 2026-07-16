"""Tests for catalog_00379."""

import pytest

from cartservice.generated.catalog_00379 import (
    Product_00379,
    bucket_by_tag_00379,
    is_valid_sku_00379,
    price_with_tax_00379,
)


def test_price_with_tax_00379():
    assert price_with_tax_00379(1000, 500) == 1050


def test_price_with_tax_negative_00379():
    with pytest.raises(ValueError):
        price_with_tax_00379(1000, -1)


def test_is_valid_sku_00379():
    assert is_valid_sku_00379("abc123")
    assert not is_valid_sku_00379("")


def test_bucket_by_tag_00379():
    p = Product_00379("s1", 100, ["a"])
    assert bucket_by_tag_00379([p]) == {"a": ["s1"]}
