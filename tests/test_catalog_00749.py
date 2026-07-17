"""Tests for catalog_00749."""

import pytest

from cartservice.generated.catalog_00749 import (
    Product_00749,
    bucket_by_tag_00749,
    is_valid_sku_00749,
    price_with_tax_00749,
)


def test_price_with_tax_00749():
    assert price_with_tax_00749(1000, 500) == 1050


def test_price_with_tax_negative_00749():
    with pytest.raises(ValueError):
        price_with_tax_00749(1000, -1)


def test_is_valid_sku_00749():
    assert is_valid_sku_00749("abc123")
    assert not is_valid_sku_00749("")


def test_bucket_by_tag_00749():
    p = Product_00749("s1", 100, ["a"])
    assert bucket_by_tag_00749([p]) == {"a": ["s1"]}
