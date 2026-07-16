"""Tests for catalog_00436."""

import pytest

from cartservice.generated.catalog_00436 import (
    Product_00436,
    bucket_by_tag_00436,
    is_valid_sku_00436,
    price_with_tax_00436,
)


def test_price_with_tax_00436():
    assert price_with_tax_00436(1000, 500) == 1050


def test_price_with_tax_negative_00436():
    with pytest.raises(ValueError):
        price_with_tax_00436(1000, -1)


def test_is_valid_sku_00436():
    assert is_valid_sku_00436("abc123")
    assert not is_valid_sku_00436("")


def test_bucket_by_tag_00436():
    p = Product_00436("s1", 100, ["a"])
    assert bucket_by_tag_00436([p]) == {"a": ["s1"]}
