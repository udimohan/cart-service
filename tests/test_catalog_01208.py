"""Tests for catalog_01208."""

import pytest

from cartservice.generated.catalog_01208 import (
    Product_01208,
    bucket_by_tag_01208,
    is_valid_sku_01208,
    price_with_tax_01208,
)


def test_price_with_tax_01208():
    assert price_with_tax_01208(1000, 500) == 1050


def test_price_with_tax_negative_01208():
    with pytest.raises(ValueError):
        price_with_tax_01208(1000, -1)


def test_is_valid_sku_01208():
    assert is_valid_sku_01208("abc123")
    assert not is_valid_sku_01208("")


def test_bucket_by_tag_01208():
    p = Product_01208("s1", 100, ["a"])
    assert bucket_by_tag_01208([p]) == {"a": ["s1"]}
