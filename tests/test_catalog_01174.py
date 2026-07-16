"""Tests for catalog_01174."""

import pytest

from cartservice.generated.catalog_01174 import (
    Product_01174,
    bucket_by_tag_01174,
    is_valid_sku_01174,
    price_with_tax_01174,
)


def test_price_with_tax_01174():
    assert price_with_tax_01174(1000, 500) == 1050


def test_price_with_tax_negative_01174():
    with pytest.raises(ValueError):
        price_with_tax_01174(1000, -1)


def test_is_valid_sku_01174():
    assert is_valid_sku_01174("abc123")
    assert not is_valid_sku_01174("")


def test_bucket_by_tag_01174():
    p = Product_01174("s1", 100, ["a"])
    assert bucket_by_tag_01174([p]) == {"a": ["s1"]}
