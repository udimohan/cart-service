"""Tests for catalog_01355."""

import pytest

from cartservice.generated.catalog_01355 import (
    Product_01355,
    bucket_by_tag_01355,
    is_valid_sku_01355,
    price_with_tax_01355,
)


def test_price_with_tax_01355():
    assert price_with_tax_01355(1000, 500) == 1050


def test_price_with_tax_negative_01355():
    with pytest.raises(ValueError):
        price_with_tax_01355(1000, -1)


def test_is_valid_sku_01355():
    assert is_valid_sku_01355("abc123")
    assert not is_valid_sku_01355("")


def test_bucket_by_tag_01355():
    p = Product_01355("s1", 100, ["a"])
    assert bucket_by_tag_01355([p]) == {"a": ["s1"]}
