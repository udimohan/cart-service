"""Tests for catalog_00458."""

import pytest

from cartservice.generated.catalog_00458 import (
    Product_00458,
    bucket_by_tag_00458,
    is_valid_sku_00458,
    price_with_tax_00458,
)


def test_price_with_tax_00458():
    assert price_with_tax_00458(1000, 500) == 1050


def test_price_with_tax_negative_00458():
    with pytest.raises(ValueError):
        price_with_tax_00458(1000, -1)


def test_is_valid_sku_00458():
    assert is_valid_sku_00458("abc123")
    assert not is_valid_sku_00458("")


def test_bucket_by_tag_00458():
    p = Product_00458("s1", 100, ["a"])
    assert bucket_by_tag_00458([p]) == {"a": ["s1"]}
