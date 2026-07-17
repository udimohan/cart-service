"""Tests for catalog_01570."""

import pytest

from cartservice.generated.catalog_01570 import (
    Product_01570,
    bucket_by_tag_01570,
    is_valid_sku_01570,
    price_with_tax_01570,
)


def test_price_with_tax_01570():
    assert price_with_tax_01570(1000, 500) == 1050


def test_price_with_tax_negative_01570():
    with pytest.raises(ValueError):
        price_with_tax_01570(1000, -1)


def test_is_valid_sku_01570():
    assert is_valid_sku_01570("abc123")
    assert not is_valid_sku_01570("")


def test_bucket_by_tag_01570():
    p = Product_01570("s1", 100, ["a"])
    assert bucket_by_tag_01570([p]) == {"a": ["s1"]}
