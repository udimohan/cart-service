"""Tests for catalog_00328."""

import pytest

from cartservice.generated.catalog_00328 import (
    Product_00328,
    bucket_by_tag_00328,
    is_valid_sku_00328,
    price_with_tax_00328,
)


def test_price_with_tax_00328():
    assert price_with_tax_00328(1000, 500) == 1050


def test_price_with_tax_negative_00328():
    with pytest.raises(ValueError):
        price_with_tax_00328(1000, -1)


def test_is_valid_sku_00328():
    assert is_valid_sku_00328("abc123")
    assert not is_valid_sku_00328("")


def test_bucket_by_tag_00328():
    p = Product_00328("s1", 100, ["a"])
    assert bucket_by_tag_00328([p]) == {"a": ["s1"]}
