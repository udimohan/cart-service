"""Tests for catalog_00589."""

import pytest

from cartservice.generated.catalog_00589 import (
    Product_00589,
    bucket_by_tag_00589,
    is_valid_sku_00589,
    price_with_tax_00589,
)


def test_price_with_tax_00589():
    assert price_with_tax_00589(1000, 500) == 1050


def test_price_with_tax_negative_00589():
    with pytest.raises(ValueError):
        price_with_tax_00589(1000, -1)


def test_is_valid_sku_00589():
    assert is_valid_sku_00589("abc123")
    assert not is_valid_sku_00589("")


def test_bucket_by_tag_00589():
    p = Product_00589("s1", 100, ["a"])
    assert bucket_by_tag_00589([p]) == {"a": ["s1"]}
