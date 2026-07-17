"""Tests for catalog_01458."""

import pytest

from cartservice.generated.catalog_01458 import (
    Product_01458,
    bucket_by_tag_01458,
    is_valid_sku_01458,
    price_with_tax_01458,
)


def test_price_with_tax_01458():
    assert price_with_tax_01458(1000, 500) == 1050


def test_price_with_tax_negative_01458():
    with pytest.raises(ValueError):
        price_with_tax_01458(1000, -1)


def test_is_valid_sku_01458():
    assert is_valid_sku_01458("abc123")
    assert not is_valid_sku_01458("")


def test_bucket_by_tag_01458():
    p = Product_01458("s1", 100, ["a"])
    assert bucket_by_tag_01458([p]) == {"a": ["s1"]}
