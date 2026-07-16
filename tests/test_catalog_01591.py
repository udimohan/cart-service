"""Tests for catalog_01591."""

import pytest

from cartservice.generated.catalog_01591 import (
    Product_01591,
    bucket_by_tag_01591,
    is_valid_sku_01591,
    price_with_tax_01591,
)


def test_price_with_tax_01591():
    assert price_with_tax_01591(1000, 500) == 1050


def test_price_with_tax_negative_01591():
    with pytest.raises(ValueError):
        price_with_tax_01591(1000, -1)


def test_is_valid_sku_01591():
    assert is_valid_sku_01591("abc123")
    assert not is_valid_sku_01591("")


def test_bucket_by_tag_01591():
    p = Product_01591("s1", 100, ["a"])
    assert bucket_by_tag_01591([p]) == {"a": ["s1"]}
