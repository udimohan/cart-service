"""Tests for catalog_00704."""

import pytest

from cartservice.generated.catalog_00704 import (
    Product_00704,
    bucket_by_tag_00704,
    is_valid_sku_00704,
    price_with_tax_00704,
)


def test_price_with_tax_00704():
    assert price_with_tax_00704(1000, 500) == 1050


def test_price_with_tax_negative_00704():
    with pytest.raises(ValueError):
        price_with_tax_00704(1000, -1)


def test_is_valid_sku_00704():
    assert is_valid_sku_00704("abc123")
    assert not is_valid_sku_00704("")


def test_bucket_by_tag_00704():
    p = Product_00704("s1", 100, ["a"])
    assert bucket_by_tag_00704([p]) == {"a": ["s1"]}
