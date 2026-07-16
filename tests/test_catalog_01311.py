"""Tests for catalog_01311."""

import pytest

from cartservice.generated.catalog_01311 import (
    Product_01311,
    bucket_by_tag_01311,
    is_valid_sku_01311,
    price_with_tax_01311,
)


def test_price_with_tax_01311():
    assert price_with_tax_01311(1000, 500) == 1050


def test_price_with_tax_negative_01311():
    with pytest.raises(ValueError):
        price_with_tax_01311(1000, -1)


def test_is_valid_sku_01311():
    assert is_valid_sku_01311("abc123")
    assert not is_valid_sku_01311("")


def test_bucket_by_tag_01311():
    p = Product_01311("s1", 100, ["a"])
    assert bucket_by_tag_01311([p]) == {"a": ["s1"]}
