"""Tests for catalog_01349."""

import pytest

from cartservice.generated.catalog_01349 import (
    Product_01349,
    bucket_by_tag_01349,
    is_valid_sku_01349,
    price_with_tax_01349,
)


def test_price_with_tax_01349():
    assert price_with_tax_01349(1000, 500) == 1050


def test_price_with_tax_negative_01349():
    with pytest.raises(ValueError):
        price_with_tax_01349(1000, -1)


def test_is_valid_sku_01349():
    assert is_valid_sku_01349("abc123")
    assert not is_valid_sku_01349("")


def test_bucket_by_tag_01349():
    p = Product_01349("s1", 100, ["a"])
    assert bucket_by_tag_01349([p]) == {"a": ["s1"]}
