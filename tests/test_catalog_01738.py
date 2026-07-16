"""Tests for catalog_01738."""

import pytest

from cartservice.generated.catalog_01738 import (
    Product_01738,
    bucket_by_tag_01738,
    is_valid_sku_01738,
    price_with_tax_01738,
)


def test_price_with_tax_01738():
    assert price_with_tax_01738(1000, 500) == 1050


def test_price_with_tax_negative_01738():
    with pytest.raises(ValueError):
        price_with_tax_01738(1000, -1)


def test_is_valid_sku_01738():
    assert is_valid_sku_01738("abc123")
    assert not is_valid_sku_01738("")


def test_bucket_by_tag_01738():
    p = Product_01738("s1", 100, ["a"])
    assert bucket_by_tag_01738([p]) == {"a": ["s1"]}
