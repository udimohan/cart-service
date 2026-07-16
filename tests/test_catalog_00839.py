"""Tests for catalog_00839."""

import pytest

from cartservice.generated.catalog_00839 import (
    Product_00839,
    bucket_by_tag_00839,
    is_valid_sku_00839,
    price_with_tax_00839,
)


def test_price_with_tax_00839():
    assert price_with_tax_00839(1000, 500) == 1050


def test_price_with_tax_negative_00839():
    with pytest.raises(ValueError):
        price_with_tax_00839(1000, -1)


def test_is_valid_sku_00839():
    assert is_valid_sku_00839("abc123")
    assert not is_valid_sku_00839("")


def test_bucket_by_tag_00839():
    p = Product_00839("s1", 100, ["a"])
    assert bucket_by_tag_00839([p]) == {"a": ["s1"]}
