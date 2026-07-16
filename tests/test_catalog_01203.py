"""Tests for catalog_01203."""

import pytest

from cartservice.generated.catalog_01203 import (
    Product_01203,
    bucket_by_tag_01203,
    is_valid_sku_01203,
    price_with_tax_01203,
)


def test_price_with_tax_01203():
    assert price_with_tax_01203(1000, 500) == 1050


def test_price_with_tax_negative_01203():
    with pytest.raises(ValueError):
        price_with_tax_01203(1000, -1)


def test_is_valid_sku_01203():
    assert is_valid_sku_01203("abc123")
    assert not is_valid_sku_01203("")


def test_bucket_by_tag_01203():
    p = Product_01203("s1", 100, ["a"])
    assert bucket_by_tag_01203([p]) == {"a": ["s1"]}
