"""Tests for catalog_00180."""

import pytest

from cartservice.generated.catalog_00180 import (
    Product_00180,
    bucket_by_tag_00180,
    is_valid_sku_00180,
    price_with_tax_00180,
)


def test_price_with_tax_00180():
    assert price_with_tax_00180(1000, 500) == 1050


def test_price_with_tax_negative_00180():
    with pytest.raises(ValueError):
        price_with_tax_00180(1000, -1)


def test_is_valid_sku_00180():
    assert is_valid_sku_00180("abc123")
    assert not is_valid_sku_00180("")


def test_bucket_by_tag_00180():
    p = Product_00180("s1", 100, ["a"])
    assert bucket_by_tag_00180([p]) == {"a": ["s1"]}
