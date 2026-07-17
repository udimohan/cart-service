"""Tests for catalog_00346."""

import pytest

from cartservice.generated.catalog_00346 import (
    Product_00346,
    bucket_by_tag_00346,
    is_valid_sku_00346,
    price_with_tax_00346,
)


def test_price_with_tax_00346():
    assert price_with_tax_00346(1000, 500) == 1050


def test_price_with_tax_negative_00346():
    with pytest.raises(ValueError):
        price_with_tax_00346(1000, -1)


def test_is_valid_sku_00346():
    assert is_valid_sku_00346("abc123")
    assert not is_valid_sku_00346("")


def test_bucket_by_tag_00346():
    p = Product_00346("s1", 100, ["a"])
    assert bucket_by_tag_00346([p]) == {"a": ["s1"]}
