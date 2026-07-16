"""Tests for catalog_00533."""

import pytest

from cartservice.generated.catalog_00533 import (
    Product_00533,
    bucket_by_tag_00533,
    is_valid_sku_00533,
    price_with_tax_00533,
)


def test_price_with_tax_00533():
    assert price_with_tax_00533(1000, 500) == 1050


def test_price_with_tax_negative_00533():
    with pytest.raises(ValueError):
        price_with_tax_00533(1000, -1)


def test_is_valid_sku_00533():
    assert is_valid_sku_00533("abc123")
    assert not is_valid_sku_00533("")


def test_bucket_by_tag_00533():
    p = Product_00533("s1", 100, ["a"])
    assert bucket_by_tag_00533([p]) == {"a": ["s1"]}
