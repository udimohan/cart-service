"""Tests for catalog_01333."""

import pytest

from cartservice.generated.catalog_01333 import (
    Product_01333,
    bucket_by_tag_01333,
    is_valid_sku_01333,
    price_with_tax_01333,
)


def test_price_with_tax_01333():
    assert price_with_tax_01333(1000, 500) == 1050


def test_price_with_tax_negative_01333():
    with pytest.raises(ValueError):
        price_with_tax_01333(1000, -1)


def test_is_valid_sku_01333():
    assert is_valid_sku_01333("abc123")
    assert not is_valid_sku_01333("")


def test_bucket_by_tag_01333():
    p = Product_01333("s1", 100, ["a"])
    assert bucket_by_tag_01333([p]) == {"a": ["s1"]}
