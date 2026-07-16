"""Tests for catalog_00745."""

import pytest

from cartservice.generated.catalog_00745 import (
    Product_00745,
    bucket_by_tag_00745,
    is_valid_sku_00745,
    price_with_tax_00745,
)


def test_price_with_tax_00745():
    assert price_with_tax_00745(1000, 500) == 1050


def test_price_with_tax_negative_00745():
    with pytest.raises(ValueError):
        price_with_tax_00745(1000, -1)


def test_is_valid_sku_00745():
    assert is_valid_sku_00745("abc123")
    assert not is_valid_sku_00745("")


def test_bucket_by_tag_00745():
    p = Product_00745("s1", 100, ["a"])
    assert bucket_by_tag_00745([p]) == {"a": ["s1"]}
