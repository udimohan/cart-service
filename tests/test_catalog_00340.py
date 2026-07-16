"""Tests for catalog_00340."""

import pytest

from cartservice.generated.catalog_00340 import (
    Product_00340,
    bucket_by_tag_00340,
    is_valid_sku_00340,
    price_with_tax_00340,
)


def test_price_with_tax_00340():
    assert price_with_tax_00340(1000, 500) == 1050


def test_price_with_tax_negative_00340():
    with pytest.raises(ValueError):
        price_with_tax_00340(1000, -1)


def test_is_valid_sku_00340():
    assert is_valid_sku_00340("abc123")
    assert not is_valid_sku_00340("")


def test_bucket_by_tag_00340():
    p = Product_00340("s1", 100, ["a"])
    assert bucket_by_tag_00340([p]) == {"a": ["s1"]}
