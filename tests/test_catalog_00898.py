"""Tests for catalog_00898."""

import pytest

from cartservice.generated.catalog_00898 import (
    Product_00898,
    bucket_by_tag_00898,
    is_valid_sku_00898,
    price_with_tax_00898,
)


def test_price_with_tax_00898():
    assert price_with_tax_00898(1000, 500) == 1050


def test_price_with_tax_negative_00898():
    with pytest.raises(ValueError):
        price_with_tax_00898(1000, -1)


def test_is_valid_sku_00898():
    assert is_valid_sku_00898("abc123")
    assert not is_valid_sku_00898("")


def test_bucket_by_tag_00898():
    p = Product_00898("s1", 100, ["a"])
    assert bucket_by_tag_00898([p]) == {"a": ["s1"]}
