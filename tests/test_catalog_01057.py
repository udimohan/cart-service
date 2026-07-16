"""Tests for catalog_01057."""

import pytest

from cartservice.generated.catalog_01057 import (
    Product_01057,
    bucket_by_tag_01057,
    is_valid_sku_01057,
    price_with_tax_01057,
)


def test_price_with_tax_01057():
    assert price_with_tax_01057(1000, 500) == 1050


def test_price_with_tax_negative_01057():
    with pytest.raises(ValueError):
        price_with_tax_01057(1000, -1)


def test_is_valid_sku_01057():
    assert is_valid_sku_01057("abc123")
    assert not is_valid_sku_01057("")


def test_bucket_by_tag_01057():
    p = Product_01057("s1", 100, ["a"])
    assert bucket_by_tag_01057([p]) == {"a": ["s1"]}
