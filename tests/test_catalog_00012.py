"""Tests for catalog_00012."""

import pytest

from cartservice.generated.catalog_00012 import (
    Product_00012,
    bucket_by_tag_00012,
    is_valid_sku_00012,
    price_with_tax_00012,
)


def test_price_with_tax_00012():
    assert price_with_tax_00012(1000, 500) == 1050


def test_price_with_tax_negative_00012():
    with pytest.raises(ValueError):
        price_with_tax_00012(1000, -1)


def test_is_valid_sku_00012():
    assert is_valid_sku_00012("abc123")
    assert not is_valid_sku_00012("")


def test_bucket_by_tag_00012():
    p = Product_00012("s1", 100, ["a"])
    assert bucket_by_tag_00012([p]) == {"a": ["s1"]}
