"""Tests for catalog_01058."""

import pytest

from cartservice.generated.catalog_01058 import (
    Product_01058,
    bucket_by_tag_01058,
    is_valid_sku_01058,
    price_with_tax_01058,
)


def test_price_with_tax_01058():
    assert price_with_tax_01058(1000, 500) == 1050


def test_price_with_tax_negative_01058():
    with pytest.raises(ValueError):
        price_with_tax_01058(1000, -1)


def test_is_valid_sku_01058():
    assert is_valid_sku_01058("abc123")
    assert not is_valid_sku_01058("")


def test_bucket_by_tag_01058():
    p = Product_01058("s1", 100, ["a"])
    assert bucket_by_tag_01058([p]) == {"a": ["s1"]}
