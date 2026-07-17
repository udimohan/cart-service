"""Tests for catalog_00098."""

import pytest

from cartservice.generated.catalog_00098 import (
    Product_00098,
    bucket_by_tag_00098,
    is_valid_sku_00098,
    price_with_tax_00098,
)


def test_price_with_tax_00098():
    assert price_with_tax_00098(1000, 500) == 1050


def test_price_with_tax_negative_00098():
    with pytest.raises(ValueError):
        price_with_tax_00098(1000, -1)


def test_is_valid_sku_00098():
    assert is_valid_sku_00098("abc123")
    assert not is_valid_sku_00098("")


def test_bucket_by_tag_00098():
    p = Product_00098("s1", 100, ["a"])
    assert bucket_by_tag_00098([p]) == {"a": ["s1"]}
