"""Tests for catalog_00676."""

import pytest

from cartservice.generated.catalog_00676 import (
    Product_00676,
    bucket_by_tag_00676,
    is_valid_sku_00676,
    price_with_tax_00676,
)


def test_price_with_tax_00676():
    assert price_with_tax_00676(1000, 500) == 1050


def test_price_with_tax_negative_00676():
    with pytest.raises(ValueError):
        price_with_tax_00676(1000, -1)


def test_is_valid_sku_00676():
    assert is_valid_sku_00676("abc123")
    assert not is_valid_sku_00676("")


def test_bucket_by_tag_00676():
    p = Product_00676("s1", 100, ["a"])
    assert bucket_by_tag_00676([p]) == {"a": ["s1"]}
