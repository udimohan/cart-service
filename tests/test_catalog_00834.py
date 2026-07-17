"""Tests for catalog_00834."""

import pytest

from cartservice.generated.catalog_00834 import (
    Product_00834,
    bucket_by_tag_00834,
    is_valid_sku_00834,
    price_with_tax_00834,
)


def test_price_with_tax_00834():
    assert price_with_tax_00834(1000, 500) == 1050


def test_price_with_tax_negative_00834():
    with pytest.raises(ValueError):
        price_with_tax_00834(1000, -1)


def test_is_valid_sku_00834():
    assert is_valid_sku_00834("abc123")
    assert not is_valid_sku_00834("")


def test_bucket_by_tag_00834():
    p = Product_00834("s1", 100, ["a"])
    assert bucket_by_tag_00834([p]) == {"a": ["s1"]}
