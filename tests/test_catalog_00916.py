"""Tests for catalog_00916."""

import pytest

from cartservice.generated.catalog_00916 import (
    Product_00916,
    bucket_by_tag_00916,
    is_valid_sku_00916,
    price_with_tax_00916,
)


def test_price_with_tax_00916():
    assert price_with_tax_00916(1000, 500) == 1050


def test_price_with_tax_negative_00916():
    with pytest.raises(ValueError):
        price_with_tax_00916(1000, -1)


def test_is_valid_sku_00916():
    assert is_valid_sku_00916("abc123")
    assert not is_valid_sku_00916("")


def test_bucket_by_tag_00916():
    p = Product_00916("s1", 100, ["a"])
    assert bucket_by_tag_00916([p]) == {"a": ["s1"]}
