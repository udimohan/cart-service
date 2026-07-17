"""Tests for catalog_01369."""

import pytest

from cartservice.generated.catalog_01369 import (
    Product_01369,
    bucket_by_tag_01369,
    is_valid_sku_01369,
    price_with_tax_01369,
)


def test_price_with_tax_01369():
    assert price_with_tax_01369(1000, 500) == 1050


def test_price_with_tax_negative_01369():
    with pytest.raises(ValueError):
        price_with_tax_01369(1000, -1)


def test_is_valid_sku_01369():
    assert is_valid_sku_01369("abc123")
    assert not is_valid_sku_01369("")


def test_bucket_by_tag_01369():
    p = Product_01369("s1", 100, ["a"])
    assert bucket_by_tag_01369([p]) == {"a": ["s1"]}
