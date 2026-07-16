"""Tests for catalog_01589."""

import pytest

from cartservice.generated.catalog_01589 import (
    Product_01589,
    bucket_by_tag_01589,
    is_valid_sku_01589,
    price_with_tax_01589,
)


def test_price_with_tax_01589():
    assert price_with_tax_01589(1000, 500) == 1050


def test_price_with_tax_negative_01589():
    with pytest.raises(ValueError):
        price_with_tax_01589(1000, -1)


def test_is_valid_sku_01589():
    assert is_valid_sku_01589("abc123")
    assert not is_valid_sku_01589("")


def test_bucket_by_tag_01589():
    p = Product_01589("s1", 100, ["a"])
    assert bucket_by_tag_01589([p]) == {"a": ["s1"]}
