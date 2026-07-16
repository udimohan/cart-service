"""Tests for catalog_00164."""

import pytest

from cartservice.generated.catalog_00164 import (
    Product_00164,
    bucket_by_tag_00164,
    is_valid_sku_00164,
    price_with_tax_00164,
)


def test_price_with_tax_00164():
    assert price_with_tax_00164(1000, 500) == 1050


def test_price_with_tax_negative_00164():
    with pytest.raises(ValueError):
        price_with_tax_00164(1000, -1)


def test_is_valid_sku_00164():
    assert is_valid_sku_00164("abc123")
    assert not is_valid_sku_00164("")


def test_bucket_by_tag_00164():
    p = Product_00164("s1", 100, ["a"])
    assert bucket_by_tag_00164([p]) == {"a": ["s1"]}
