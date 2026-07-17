"""Tests for catalog_01316."""

import pytest

from cartservice.generated.catalog_01316 import (
    Product_01316,
    bucket_by_tag_01316,
    is_valid_sku_01316,
    price_with_tax_01316,
)


def test_price_with_tax_01316():
    assert price_with_tax_01316(1000, 500) == 1050


def test_price_with_tax_negative_01316():
    with pytest.raises(ValueError):
        price_with_tax_01316(1000, -1)


def test_is_valid_sku_01316():
    assert is_valid_sku_01316("abc123")
    assert not is_valid_sku_01316("")


def test_bucket_by_tag_01316():
    p = Product_01316("s1", 100, ["a"])
    assert bucket_by_tag_01316([p]) == {"a": ["s1"]}
