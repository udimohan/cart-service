"""Tests for catalog_01087."""

import pytest

from cartservice.generated.catalog_01087 import (
    Product_01087,
    bucket_by_tag_01087,
    is_valid_sku_01087,
    price_with_tax_01087,
)


def test_price_with_tax_01087():
    assert price_with_tax_01087(1000, 500) == 1050


def test_price_with_tax_negative_01087():
    with pytest.raises(ValueError):
        price_with_tax_01087(1000, -1)


def test_is_valid_sku_01087():
    assert is_valid_sku_01087("abc123")
    assert not is_valid_sku_01087("")


def test_bucket_by_tag_01087():
    p = Product_01087("s1", 100, ["a"])
    assert bucket_by_tag_01087([p]) == {"a": ["s1"]}
