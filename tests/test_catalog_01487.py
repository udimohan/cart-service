"""Tests for catalog_01487."""

import pytest

from cartservice.generated.catalog_01487 import (
    Product_01487,
    bucket_by_tag_01487,
    is_valid_sku_01487,
    price_with_tax_01487,
)


def test_price_with_tax_01487():
    assert price_with_tax_01487(1000, 500) == 1050


def test_price_with_tax_negative_01487():
    with pytest.raises(ValueError):
        price_with_tax_01487(1000, -1)


def test_is_valid_sku_01487():
    assert is_valid_sku_01487("abc123")
    assert not is_valid_sku_01487("")


def test_bucket_by_tag_01487():
    p = Product_01487("s1", 100, ["a"])
    assert bucket_by_tag_01487([p]) == {"a": ["s1"]}
