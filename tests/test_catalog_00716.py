"""Tests for catalog_00716."""

import pytest

from cartservice.generated.catalog_00716 import (
    Product_00716,
    bucket_by_tag_00716,
    is_valid_sku_00716,
    price_with_tax_00716,
)


def test_price_with_tax_00716():
    assert price_with_tax_00716(1000, 500) == 1050


def test_price_with_tax_negative_00716():
    with pytest.raises(ValueError):
        price_with_tax_00716(1000, -1)


def test_is_valid_sku_00716():
    assert is_valid_sku_00716("abc123")
    assert not is_valid_sku_00716("")


def test_bucket_by_tag_00716():
    p = Product_00716("s1", 100, ["a"])
    assert bucket_by_tag_00716([p]) == {"a": ["s1"]}
