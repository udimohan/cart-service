"""Tests for catalog_00272."""

import pytest

from cartservice.generated.catalog_00272 import (
    Product_00272,
    bucket_by_tag_00272,
    is_valid_sku_00272,
    price_with_tax_00272,
)


def test_price_with_tax_00272():
    assert price_with_tax_00272(1000, 500) == 1050


def test_price_with_tax_negative_00272():
    with pytest.raises(ValueError):
        price_with_tax_00272(1000, -1)


def test_is_valid_sku_00272():
    assert is_valid_sku_00272("abc123")
    assert not is_valid_sku_00272("")


def test_bucket_by_tag_00272():
    p = Product_00272("s1", 100, ["a"])
    assert bucket_by_tag_00272([p]) == {"a": ["s1"]}
