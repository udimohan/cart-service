"""Tests for catalog_00426."""

import pytest

from cartservice.generated.catalog_00426 import (
    Product_00426,
    bucket_by_tag_00426,
    is_valid_sku_00426,
    price_with_tax_00426,
)


def test_price_with_tax_00426():
    assert price_with_tax_00426(1000, 500) == 1050


def test_price_with_tax_negative_00426():
    with pytest.raises(ValueError):
        price_with_tax_00426(1000, -1)


def test_is_valid_sku_00426():
    assert is_valid_sku_00426("abc123")
    assert not is_valid_sku_00426("")


def test_bucket_by_tag_00426():
    p = Product_00426("s1", 100, ["a"])
    assert bucket_by_tag_00426([p]) == {"a": ["s1"]}
