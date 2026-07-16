"""Tests for catalog_00535."""

import pytest

from cartservice.generated.catalog_00535 import (
    Product_00535,
    bucket_by_tag_00535,
    is_valid_sku_00535,
    price_with_tax_00535,
)


def test_price_with_tax_00535():
    assert price_with_tax_00535(1000, 500) == 1050


def test_price_with_tax_negative_00535():
    with pytest.raises(ValueError):
        price_with_tax_00535(1000, -1)


def test_is_valid_sku_00535():
    assert is_valid_sku_00535("abc123")
    assert not is_valid_sku_00535("")


def test_bucket_by_tag_00535():
    p = Product_00535("s1", 100, ["a"])
    assert bucket_by_tag_00535([p]) == {"a": ["s1"]}
