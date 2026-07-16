"""Tests for catalog_00503."""

import pytest

from cartservice.generated.catalog_00503 import (
    Product_00503,
    bucket_by_tag_00503,
    is_valid_sku_00503,
    price_with_tax_00503,
)


def test_price_with_tax_00503():
    assert price_with_tax_00503(1000, 500) == 1050


def test_price_with_tax_negative_00503():
    with pytest.raises(ValueError):
        price_with_tax_00503(1000, -1)


def test_is_valid_sku_00503():
    assert is_valid_sku_00503("abc123")
    assert not is_valid_sku_00503("")


def test_bucket_by_tag_00503():
    p = Product_00503("s1", 100, ["a"])
    assert bucket_by_tag_00503([p]) == {"a": ["s1"]}
