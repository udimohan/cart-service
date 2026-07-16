"""Tests for catalog_00393."""

import pytest

from cartservice.generated.catalog_00393 import (
    Product_00393,
    bucket_by_tag_00393,
    is_valid_sku_00393,
    price_with_tax_00393,
)


def test_price_with_tax_00393():
    assert price_with_tax_00393(1000, 500) == 1050


def test_price_with_tax_negative_00393():
    with pytest.raises(ValueError):
        price_with_tax_00393(1000, -1)


def test_is_valid_sku_00393():
    assert is_valid_sku_00393("abc123")
    assert not is_valid_sku_00393("")


def test_bucket_by_tag_00393():
    p = Product_00393("s1", 100, ["a"])
    assert bucket_by_tag_00393([p]) == {"a": ["s1"]}
