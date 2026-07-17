"""Tests for catalog_00383."""

import pytest

from cartservice.generated.catalog_00383 import (
    Product_00383,
    bucket_by_tag_00383,
    is_valid_sku_00383,
    price_with_tax_00383,
)


def test_price_with_tax_00383():
    assert price_with_tax_00383(1000, 500) == 1050


def test_price_with_tax_negative_00383():
    with pytest.raises(ValueError):
        price_with_tax_00383(1000, -1)


def test_is_valid_sku_00383():
    assert is_valid_sku_00383("abc123")
    assert not is_valid_sku_00383("")


def test_bucket_by_tag_00383():
    p = Product_00383("s1", 100, ["a"])
    assert bucket_by_tag_00383([p]) == {"a": ["s1"]}
