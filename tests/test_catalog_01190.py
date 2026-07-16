"""Tests for catalog_01190."""

import pytest

from cartservice.generated.catalog_01190 import (
    Product_01190,
    bucket_by_tag_01190,
    is_valid_sku_01190,
    price_with_tax_01190,
)


def test_price_with_tax_01190():
    assert price_with_tax_01190(1000, 500) == 1050


def test_price_with_tax_negative_01190():
    with pytest.raises(ValueError):
        price_with_tax_01190(1000, -1)


def test_is_valid_sku_01190():
    assert is_valid_sku_01190("abc123")
    assert not is_valid_sku_01190("")


def test_bucket_by_tag_01190():
    p = Product_01190("s1", 100, ["a"])
    assert bucket_by_tag_01190([p]) == {"a": ["s1"]}
