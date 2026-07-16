"""Tests for catalog_00972."""

import pytest

from cartservice.generated.catalog_00972 import (
    Product_00972,
    bucket_by_tag_00972,
    is_valid_sku_00972,
    price_with_tax_00972,
)


def test_price_with_tax_00972():
    assert price_with_tax_00972(1000, 500) == 1050


def test_price_with_tax_negative_00972():
    with pytest.raises(ValueError):
        price_with_tax_00972(1000, -1)


def test_is_valid_sku_00972():
    assert is_valid_sku_00972("abc123")
    assert not is_valid_sku_00972("")


def test_bucket_by_tag_00972():
    p = Product_00972("s1", 100, ["a"])
    assert bucket_by_tag_00972([p]) == {"a": ["s1"]}
