"""Tests for catalog_01687."""

import pytest

from cartservice.generated.catalog_01687 import (
    Product_01687,
    bucket_by_tag_01687,
    is_valid_sku_01687,
    price_with_tax_01687,
)


def test_price_with_tax_01687():
    assert price_with_tax_01687(1000, 500) == 1050


def test_price_with_tax_negative_01687():
    with pytest.raises(ValueError):
        price_with_tax_01687(1000, -1)


def test_is_valid_sku_01687():
    assert is_valid_sku_01687("abc123")
    assert not is_valid_sku_01687("")


def test_bucket_by_tag_01687():
    p = Product_01687("s1", 100, ["a"])
    assert bucket_by_tag_01687([p]) == {"a": ["s1"]}
