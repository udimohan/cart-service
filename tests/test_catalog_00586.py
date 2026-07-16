"""Tests for catalog_00586."""

import pytest

from cartservice.generated.catalog_00586 import (
    Product_00586,
    bucket_by_tag_00586,
    is_valid_sku_00586,
    price_with_tax_00586,
)


def test_price_with_tax_00586():
    assert price_with_tax_00586(1000, 500) == 1050


def test_price_with_tax_negative_00586():
    with pytest.raises(ValueError):
        price_with_tax_00586(1000, -1)


def test_is_valid_sku_00586():
    assert is_valid_sku_00586("abc123")
    assert not is_valid_sku_00586("")


def test_bucket_by_tag_00586():
    p = Product_00586("s1", 100, ["a"])
    assert bucket_by_tag_00586([p]) == {"a": ["s1"]}
