"""Tests for catalog_00651."""

import pytest

from cartservice.generated.catalog_00651 import (
    Product_00651,
    bucket_by_tag_00651,
    is_valid_sku_00651,
    price_with_tax_00651,
)


def test_price_with_tax_00651():
    assert price_with_tax_00651(1000, 500) == 1050


def test_price_with_tax_negative_00651():
    with pytest.raises(ValueError):
        price_with_tax_00651(1000, -1)


def test_is_valid_sku_00651():
    assert is_valid_sku_00651("abc123")
    assert not is_valid_sku_00651("")


def test_bucket_by_tag_00651():
    p = Product_00651("s1", 100, ["a"])
    assert bucket_by_tag_00651([p]) == {"a": ["s1"]}
