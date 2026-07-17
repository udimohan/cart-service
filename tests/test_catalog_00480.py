"""Tests for catalog_00480."""

import pytest

from cartservice.generated.catalog_00480 import (
    Product_00480,
    bucket_by_tag_00480,
    is_valid_sku_00480,
    price_with_tax_00480,
)


def test_price_with_tax_00480():
    assert price_with_tax_00480(1000, 500) == 1050


def test_price_with_tax_negative_00480():
    with pytest.raises(ValueError):
        price_with_tax_00480(1000, -1)


def test_is_valid_sku_00480():
    assert is_valid_sku_00480("abc123")
    assert not is_valid_sku_00480("")


def test_bucket_by_tag_00480():
    p = Product_00480("s1", 100, ["a"])
    assert bucket_by_tag_00480([p]) == {"a": ["s1"]}
