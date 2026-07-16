"""Tests for catalog_00784."""

import pytest

from cartservice.generated.catalog_00784 import (
    Product_00784,
    bucket_by_tag_00784,
    is_valid_sku_00784,
    price_with_tax_00784,
)


def test_price_with_tax_00784():
    assert price_with_tax_00784(1000, 500) == 1050


def test_price_with_tax_negative_00784():
    with pytest.raises(ValueError):
        price_with_tax_00784(1000, -1)


def test_is_valid_sku_00784():
    assert is_valid_sku_00784("abc123")
    assert not is_valid_sku_00784("")


def test_bucket_by_tag_00784():
    p = Product_00784("s1", 100, ["a"])
    assert bucket_by_tag_00784([p]) == {"a": ["s1"]}
