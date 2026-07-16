"""Tests for catalog_01571."""

import pytest

from cartservice.generated.catalog_01571 import (
    Product_01571,
    bucket_by_tag_01571,
    is_valid_sku_01571,
    price_with_tax_01571,
)


def test_price_with_tax_01571():
    assert price_with_tax_01571(1000, 500) == 1050


def test_price_with_tax_negative_01571():
    with pytest.raises(ValueError):
        price_with_tax_01571(1000, -1)


def test_is_valid_sku_01571():
    assert is_valid_sku_01571("abc123")
    assert not is_valid_sku_01571("")


def test_bucket_by_tag_01571():
    p = Product_01571("s1", 100, ["a"])
    assert bucket_by_tag_01571([p]) == {"a": ["s1"]}
