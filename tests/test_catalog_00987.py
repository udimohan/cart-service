"""Tests for catalog_00987."""

import pytest

from cartservice.generated.catalog_00987 import (
    Product_00987,
    bucket_by_tag_00987,
    is_valid_sku_00987,
    price_with_tax_00987,
)


def test_price_with_tax_00987():
    assert price_with_tax_00987(1000, 500) == 1050


def test_price_with_tax_negative_00987():
    with pytest.raises(ValueError):
        price_with_tax_00987(1000, -1)


def test_is_valid_sku_00987():
    assert is_valid_sku_00987("abc123")
    assert not is_valid_sku_00987("")


def test_bucket_by_tag_00987():
    p = Product_00987("s1", 100, ["a"])
    assert bucket_by_tag_00987([p]) == {"a": ["s1"]}
