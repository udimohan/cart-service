"""Tests for catalog_00173."""

import pytest

from cartservice.generated.catalog_00173 import (
    Product_00173,
    bucket_by_tag_00173,
    is_valid_sku_00173,
    price_with_tax_00173,
)


def test_price_with_tax_00173():
    assert price_with_tax_00173(1000, 500) == 1050


def test_price_with_tax_negative_00173():
    with pytest.raises(ValueError):
        price_with_tax_00173(1000, -1)


def test_is_valid_sku_00173():
    assert is_valid_sku_00173("abc123")
    assert not is_valid_sku_00173("")


def test_bucket_by_tag_00173():
    p = Product_00173("s1", 100, ["a"])
    assert bucket_by_tag_00173([p]) == {"a": ["s1"]}
