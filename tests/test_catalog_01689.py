"""Tests for catalog_01689."""

import pytest

from cartservice.generated.catalog_01689 import (
    Product_01689,
    bucket_by_tag_01689,
    is_valid_sku_01689,
    price_with_tax_01689,
)


def test_price_with_tax_01689():
    assert price_with_tax_01689(1000, 500) == 1050


def test_price_with_tax_negative_01689():
    with pytest.raises(ValueError):
        price_with_tax_01689(1000, -1)


def test_is_valid_sku_01689():
    assert is_valid_sku_01689("abc123")
    assert not is_valid_sku_01689("")


def test_bucket_by_tag_01689():
    p = Product_01689("s1", 100, ["a"])
    assert bucket_by_tag_01689([p]) == {"a": ["s1"]}
