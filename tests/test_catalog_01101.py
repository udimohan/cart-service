"""Tests for catalog_01101."""

import pytest

from cartservice.generated.catalog_01101 import (
    Product_01101,
    bucket_by_tag_01101,
    is_valid_sku_01101,
    price_with_tax_01101,
)


def test_price_with_tax_01101():
    assert price_with_tax_01101(1000, 500) == 1050


def test_price_with_tax_negative_01101():
    with pytest.raises(ValueError):
        price_with_tax_01101(1000, -1)


def test_is_valid_sku_01101():
    assert is_valid_sku_01101("abc123")
    assert not is_valid_sku_01101("")


def test_bucket_by_tag_01101():
    p = Product_01101("s1", 100, ["a"])
    assert bucket_by_tag_01101([p]) == {"a": ["s1"]}
