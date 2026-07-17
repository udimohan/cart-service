"""Tests for catalog_00424."""

import pytest

from cartservice.generated.catalog_00424 import (
    Product_00424,
    bucket_by_tag_00424,
    is_valid_sku_00424,
    price_with_tax_00424,
)


def test_price_with_tax_00424():
    assert price_with_tax_00424(1000, 500) == 1050


def test_price_with_tax_negative_00424():
    with pytest.raises(ValueError):
        price_with_tax_00424(1000, -1)


def test_is_valid_sku_00424():
    assert is_valid_sku_00424("abc123")
    assert not is_valid_sku_00424("")


def test_bucket_by_tag_00424():
    p = Product_00424("s1", 100, ["a"])
    assert bucket_by_tag_00424([p]) == {"a": ["s1"]}
