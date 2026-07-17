"""Tests for catalog_00303."""

import pytest

from cartservice.generated.catalog_00303 import (
    Product_00303,
    bucket_by_tag_00303,
    is_valid_sku_00303,
    price_with_tax_00303,
)


def test_price_with_tax_00303():
    assert price_with_tax_00303(1000, 500) == 1050


def test_price_with_tax_negative_00303():
    with pytest.raises(ValueError):
        price_with_tax_00303(1000, -1)


def test_is_valid_sku_00303():
    assert is_valid_sku_00303("abc123")
    assert not is_valid_sku_00303("")


def test_bucket_by_tag_00303():
    p = Product_00303("s1", 100, ["a"])
    assert bucket_by_tag_00303([p]) == {"a": ["s1"]}
