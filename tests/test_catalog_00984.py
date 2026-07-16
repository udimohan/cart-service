"""Tests for catalog_00984."""

import pytest

from cartservice.generated.catalog_00984 import (
    Product_00984,
    bucket_by_tag_00984,
    is_valid_sku_00984,
    price_with_tax_00984,
)


def test_price_with_tax_00984():
    assert price_with_tax_00984(1000, 500) == 1050


def test_price_with_tax_negative_00984():
    with pytest.raises(ValueError):
        price_with_tax_00984(1000, -1)


def test_is_valid_sku_00984():
    assert is_valid_sku_00984("abc123")
    assert not is_valid_sku_00984("")


def test_bucket_by_tag_00984():
    p = Product_00984("s1", 100, ["a"])
    assert bucket_by_tag_00984([p]) == {"a": ["s1"]}
