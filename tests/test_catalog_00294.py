"""Tests for catalog_00294."""

import pytest

from cartservice.generated.catalog_00294 import (
    Product_00294,
    bucket_by_tag_00294,
    is_valid_sku_00294,
    price_with_tax_00294,
)


def test_price_with_tax_00294():
    assert price_with_tax_00294(1000, 500) == 1050


def test_price_with_tax_negative_00294():
    with pytest.raises(ValueError):
        price_with_tax_00294(1000, -1)


def test_is_valid_sku_00294():
    assert is_valid_sku_00294("abc123")
    assert not is_valid_sku_00294("")


def test_bucket_by_tag_00294():
    p = Product_00294("s1", 100, ["a"])
    assert bucket_by_tag_00294([p]) == {"a": ["s1"]}
