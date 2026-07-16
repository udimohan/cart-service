"""Tests for catalog_01027."""

import pytest

from cartservice.generated.catalog_01027 import (
    Product_01027,
    bucket_by_tag_01027,
    is_valid_sku_01027,
    price_with_tax_01027,
)


def test_price_with_tax_01027():
    assert price_with_tax_01027(1000, 500) == 1050


def test_price_with_tax_negative_01027():
    with pytest.raises(ValueError):
        price_with_tax_01027(1000, -1)


def test_is_valid_sku_01027():
    assert is_valid_sku_01027("abc123")
    assert not is_valid_sku_01027("")


def test_bucket_by_tag_01027():
    p = Product_01027("s1", 100, ["a"])
    assert bucket_by_tag_01027([p]) == {"a": ["s1"]}
