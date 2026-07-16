"""Tests for catalog_01681."""

import pytest

from cartservice.generated.catalog_01681 import (
    Product_01681,
    bucket_by_tag_01681,
    is_valid_sku_01681,
    price_with_tax_01681,
)


def test_price_with_tax_01681():
    assert price_with_tax_01681(1000, 500) == 1050


def test_price_with_tax_negative_01681():
    with pytest.raises(ValueError):
        price_with_tax_01681(1000, -1)


def test_is_valid_sku_01681():
    assert is_valid_sku_01681("abc123")
    assert not is_valid_sku_01681("")


def test_bucket_by_tag_01681():
    p = Product_01681("s1", 100, ["a"])
    assert bucket_by_tag_01681([p]) == {"a": ["s1"]}
