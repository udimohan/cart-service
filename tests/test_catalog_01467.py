"""Tests for catalog_01467."""

import pytest

from cartservice.generated.catalog_01467 import (
    Product_01467,
    bucket_by_tag_01467,
    is_valid_sku_01467,
    price_with_tax_01467,
)


def test_price_with_tax_01467():
    assert price_with_tax_01467(1000, 500) == 1050


def test_price_with_tax_negative_01467():
    with pytest.raises(ValueError):
        price_with_tax_01467(1000, -1)


def test_is_valid_sku_01467():
    assert is_valid_sku_01467("abc123")
    assert not is_valid_sku_01467("")


def test_bucket_by_tag_01467():
    p = Product_01467("s1", 100, ["a"])
    assert bucket_by_tag_01467([p]) == {"a": ["s1"]}
