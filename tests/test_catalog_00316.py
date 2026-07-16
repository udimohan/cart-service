"""Tests for catalog_00316."""

import pytest

from cartservice.generated.catalog_00316 import (
    Product_00316,
    bucket_by_tag_00316,
    is_valid_sku_00316,
    price_with_tax_00316,
)


def test_price_with_tax_00316():
    assert price_with_tax_00316(1000, 500) == 1050


def test_price_with_tax_negative_00316():
    with pytest.raises(ValueError):
        price_with_tax_00316(1000, -1)


def test_is_valid_sku_00316():
    assert is_valid_sku_00316("abc123")
    assert not is_valid_sku_00316("")


def test_bucket_by_tag_00316():
    p = Product_00316("s1", 100, ["a"])
    assert bucket_by_tag_00316([p]) == {"a": ["s1"]}
