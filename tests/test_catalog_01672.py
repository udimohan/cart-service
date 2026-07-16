"""Tests for catalog_01672."""

import pytest

from cartservice.generated.catalog_01672 import (
    Product_01672,
    bucket_by_tag_01672,
    is_valid_sku_01672,
    price_with_tax_01672,
)


def test_price_with_tax_01672():
    assert price_with_tax_01672(1000, 500) == 1050


def test_price_with_tax_negative_01672():
    with pytest.raises(ValueError):
        price_with_tax_01672(1000, -1)


def test_is_valid_sku_01672():
    assert is_valid_sku_01672("abc123")
    assert not is_valid_sku_01672("")


def test_bucket_by_tag_01672():
    p = Product_01672("s1", 100, ["a"])
    assert bucket_by_tag_01672([p]) == {"a": ["s1"]}
