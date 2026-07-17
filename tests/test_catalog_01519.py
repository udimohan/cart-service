"""Tests for catalog_01519."""

import pytest

from cartservice.generated.catalog_01519 import (
    Product_01519,
    bucket_by_tag_01519,
    is_valid_sku_01519,
    price_with_tax_01519,
)


def test_price_with_tax_01519():
    assert price_with_tax_01519(1000, 500) == 1050


def test_price_with_tax_negative_01519():
    with pytest.raises(ValueError):
        price_with_tax_01519(1000, -1)


def test_is_valid_sku_01519():
    assert is_valid_sku_01519("abc123")
    assert not is_valid_sku_01519("")


def test_bucket_by_tag_01519():
    p = Product_01519("s1", 100, ["a"])
    assert bucket_by_tag_01519([p]) == {"a": ["s1"]}
