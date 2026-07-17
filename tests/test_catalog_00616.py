"""Tests for catalog_00616."""

import pytest

from cartservice.generated.catalog_00616 import (
    Product_00616,
    bucket_by_tag_00616,
    is_valid_sku_00616,
    price_with_tax_00616,
)


def test_price_with_tax_00616():
    assert price_with_tax_00616(1000, 500) == 1050


def test_price_with_tax_negative_00616():
    with pytest.raises(ValueError):
        price_with_tax_00616(1000, -1)


def test_is_valid_sku_00616():
    assert is_valid_sku_00616("abc123")
    assert not is_valid_sku_00616("")


def test_bucket_by_tag_00616():
    p = Product_00616("s1", 100, ["a"])
    assert bucket_by_tag_00616([p]) == {"a": ["s1"]}
