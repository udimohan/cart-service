"""Tests for catalog_00977."""

import pytest

from cartservice.generated.catalog_00977 import (
    Product_00977,
    bucket_by_tag_00977,
    is_valid_sku_00977,
    price_with_tax_00977,
)


def test_price_with_tax_00977():
    assert price_with_tax_00977(1000, 500) == 1050


def test_price_with_tax_negative_00977():
    with pytest.raises(ValueError):
        price_with_tax_00977(1000, -1)


def test_is_valid_sku_00977():
    assert is_valid_sku_00977("abc123")
    assert not is_valid_sku_00977("")


def test_bucket_by_tag_00977():
    p = Product_00977("s1", 100, ["a"])
    assert bucket_by_tag_00977([p]) == {"a": ["s1"]}
