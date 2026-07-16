"""Tests for catalog_01163."""

import pytest

from cartservice.generated.catalog_01163 import (
    Product_01163,
    bucket_by_tag_01163,
    is_valid_sku_01163,
    price_with_tax_01163,
)


def test_price_with_tax_01163():
    assert price_with_tax_01163(1000, 500) == 1050


def test_price_with_tax_negative_01163():
    with pytest.raises(ValueError):
        price_with_tax_01163(1000, -1)


def test_is_valid_sku_01163():
    assert is_valid_sku_01163("abc123")
    assert not is_valid_sku_01163("")


def test_bucket_by_tag_01163():
    p = Product_01163("s1", 100, ["a"])
    assert bucket_by_tag_01163([p]) == {"a": ["s1"]}
