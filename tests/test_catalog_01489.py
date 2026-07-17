"""Tests for catalog_01489."""

import pytest

from cartservice.generated.catalog_01489 import (
    Product_01489,
    bucket_by_tag_01489,
    is_valid_sku_01489,
    price_with_tax_01489,
)


def test_price_with_tax_01489():
    assert price_with_tax_01489(1000, 500) == 1050


def test_price_with_tax_negative_01489():
    with pytest.raises(ValueError):
        price_with_tax_01489(1000, -1)


def test_is_valid_sku_01489():
    assert is_valid_sku_01489("abc123")
    assert not is_valid_sku_01489("")


def test_bucket_by_tag_01489():
    p = Product_01489("s1", 100, ["a"])
    assert bucket_by_tag_01489([p]) == {"a": ["s1"]}
