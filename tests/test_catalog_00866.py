"""Tests for catalog_00866."""

import pytest

from cartservice.generated.catalog_00866 import (
    Product_00866,
    bucket_by_tag_00866,
    is_valid_sku_00866,
    price_with_tax_00866,
)


def test_price_with_tax_00866():
    assert price_with_tax_00866(1000, 500) == 1050


def test_price_with_tax_negative_00866():
    with pytest.raises(ValueError):
        price_with_tax_00866(1000, -1)


def test_is_valid_sku_00866():
    assert is_valid_sku_00866("abc123")
    assert not is_valid_sku_00866("")


def test_bucket_by_tag_00866():
    p = Product_00866("s1", 100, ["a"])
    assert bucket_by_tag_00866([p]) == {"a": ["s1"]}
