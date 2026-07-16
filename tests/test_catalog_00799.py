"""Tests for catalog_00799."""

import pytest

from cartservice.generated.catalog_00799 import (
    Product_00799,
    bucket_by_tag_00799,
    is_valid_sku_00799,
    price_with_tax_00799,
)


def test_price_with_tax_00799():
    assert price_with_tax_00799(1000, 500) == 1050


def test_price_with_tax_negative_00799():
    with pytest.raises(ValueError):
        price_with_tax_00799(1000, -1)


def test_is_valid_sku_00799():
    assert is_valid_sku_00799("abc123")
    assert not is_valid_sku_00799("")


def test_bucket_by_tag_00799():
    p = Product_00799("s1", 100, ["a"])
    assert bucket_by_tag_00799([p]) == {"a": ["s1"]}
