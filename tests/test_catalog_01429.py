"""Tests for catalog_01429."""

import pytest

from cartservice.generated.catalog_01429 import (
    Product_01429,
    bucket_by_tag_01429,
    is_valid_sku_01429,
    price_with_tax_01429,
)


def test_price_with_tax_01429():
    assert price_with_tax_01429(1000, 500) == 1050


def test_price_with_tax_negative_01429():
    with pytest.raises(ValueError):
        price_with_tax_01429(1000, -1)


def test_is_valid_sku_01429():
    assert is_valid_sku_01429("abc123")
    assert not is_valid_sku_01429("")


def test_bucket_by_tag_01429():
    p = Product_01429("s1", 100, ["a"])
    assert bucket_by_tag_01429([p]) == {"a": ["s1"]}
