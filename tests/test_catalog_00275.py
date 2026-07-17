"""Tests for catalog_00275."""

import pytest

from cartservice.generated.catalog_00275 import (
    Product_00275,
    bucket_by_tag_00275,
    is_valid_sku_00275,
    price_with_tax_00275,
)


def test_price_with_tax_00275():
    assert price_with_tax_00275(1000, 500) == 1050


def test_price_with_tax_negative_00275():
    with pytest.raises(ValueError):
        price_with_tax_00275(1000, -1)


def test_is_valid_sku_00275():
    assert is_valid_sku_00275("abc123")
    assert not is_valid_sku_00275("")


def test_bucket_by_tag_00275():
    p = Product_00275("s1", 100, ["a"])
    assert bucket_by_tag_00275([p]) == {"a": ["s1"]}
