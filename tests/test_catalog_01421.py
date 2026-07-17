"""Tests for catalog_01421."""

import pytest

from cartservice.generated.catalog_01421 import (
    Product_01421,
    bucket_by_tag_01421,
    is_valid_sku_01421,
    price_with_tax_01421,
)


def test_price_with_tax_01421():
    assert price_with_tax_01421(1000, 500) == 1050


def test_price_with_tax_negative_01421():
    with pytest.raises(ValueError):
        price_with_tax_01421(1000, -1)


def test_is_valid_sku_01421():
    assert is_valid_sku_01421("abc123")
    assert not is_valid_sku_01421("")


def test_bucket_by_tag_01421():
    p = Product_01421("s1", 100, ["a"])
    assert bucket_by_tag_01421([p]) == {"a": ["s1"]}
