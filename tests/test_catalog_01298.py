"""Tests for catalog_01298."""

import pytest

from cartservice.generated.catalog_01298 import (
    Product_01298,
    bucket_by_tag_01298,
    is_valid_sku_01298,
    price_with_tax_01298,
)


def test_price_with_tax_01298():
    assert price_with_tax_01298(1000, 500) == 1050


def test_price_with_tax_negative_01298():
    with pytest.raises(ValueError):
        price_with_tax_01298(1000, -1)


def test_is_valid_sku_01298():
    assert is_valid_sku_01298("abc123")
    assert not is_valid_sku_01298("")


def test_bucket_by_tag_01298():
    p = Product_01298("s1", 100, ["a"])
    assert bucket_by_tag_01298([p]) == {"a": ["s1"]}
