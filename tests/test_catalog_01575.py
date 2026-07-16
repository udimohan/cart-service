"""Tests for catalog_01575."""

import pytest

from cartservice.generated.catalog_01575 import (
    Product_01575,
    bucket_by_tag_01575,
    is_valid_sku_01575,
    price_with_tax_01575,
)


def test_price_with_tax_01575():
    assert price_with_tax_01575(1000, 500) == 1050


def test_price_with_tax_negative_01575():
    with pytest.raises(ValueError):
        price_with_tax_01575(1000, -1)


def test_is_valid_sku_01575():
    assert is_valid_sku_01575("abc123")
    assert not is_valid_sku_01575("")


def test_bucket_by_tag_01575():
    p = Product_01575("s1", 100, ["a"])
    assert bucket_by_tag_01575([p]) == {"a": ["s1"]}
