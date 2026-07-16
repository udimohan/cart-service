"""Tests for catalog_00705."""

import pytest

from cartservice.generated.catalog_00705 import (
    Product_00705,
    bucket_by_tag_00705,
    is_valid_sku_00705,
    price_with_tax_00705,
)


def test_price_with_tax_00705():
    assert price_with_tax_00705(1000, 500) == 1050


def test_price_with_tax_negative_00705():
    with pytest.raises(ValueError):
        price_with_tax_00705(1000, -1)


def test_is_valid_sku_00705():
    assert is_valid_sku_00705("abc123")
    assert not is_valid_sku_00705("")


def test_bucket_by_tag_00705():
    p = Product_00705("s1", 100, ["a"])
    assert bucket_by_tag_00705([p]) == {"a": ["s1"]}
