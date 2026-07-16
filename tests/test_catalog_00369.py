"""Tests for catalog_00369."""

import pytest

from cartservice.generated.catalog_00369 import (
    Product_00369,
    bucket_by_tag_00369,
    is_valid_sku_00369,
    price_with_tax_00369,
)


def test_price_with_tax_00369():
    assert price_with_tax_00369(1000, 500) == 1050


def test_price_with_tax_negative_00369():
    with pytest.raises(ValueError):
        price_with_tax_00369(1000, -1)


def test_is_valid_sku_00369():
    assert is_valid_sku_00369("abc123")
    assert not is_valid_sku_00369("")


def test_bucket_by_tag_00369():
    p = Product_00369("s1", 100, ["a"])
    assert bucket_by_tag_00369([p]) == {"a": ["s1"]}
