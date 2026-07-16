"""Tests for catalog_01426."""

import pytest

from cartservice.generated.catalog_01426 import (
    Product_01426,
    bucket_by_tag_01426,
    is_valid_sku_01426,
    price_with_tax_01426,
)


def test_price_with_tax_01426():
    assert price_with_tax_01426(1000, 500) == 1050


def test_price_with_tax_negative_01426():
    with pytest.raises(ValueError):
        price_with_tax_01426(1000, -1)


def test_is_valid_sku_01426():
    assert is_valid_sku_01426("abc123")
    assert not is_valid_sku_01426("")


def test_bucket_by_tag_01426():
    p = Product_01426("s1", 100, ["a"])
    assert bucket_by_tag_01426([p]) == {"a": ["s1"]}
